# auth/serializers.py
from rest_framework import serializers
from .models import User, Professeur, Centre, Etudiant

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.delete()

class ProfesseurSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Professeur
        fields = ['user', 'experience', 'cv', 'remote', 'specialty', 'phone']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        professeur = Professeur.objects.create(user=user, **validated_data)
        return professeur

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        # Update user fields
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        # Update professeur fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance
    
    def delete(self, instance):
        instance.delete()
    
class CentreSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Centre
        fields = ['user', 'address', 'capacity','phone', 'city']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        centre = Centre.objects.create(user=user, **validated_data)
        return centre
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        # Update user fields
        for attr, value in user_data.items():
            if attr == 'password':
                user.set_password(value)
            else:
                setattr(user, attr, value)
        user.save()

        # Update Centre fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        
        return instance
    
    def delete(self, instance):
        instance.delete()


class EtudiantSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Etudiant
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        etudiant = Etudiant.objects.create(user=user)
        return etudiant
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        instance.save()

        user.name = user_data.get('name', user.name)
        user.email = user_data.get('email', user.email)
        user.set_password(user_data.get('password'))
        user.save()

        return instance
    
    def delete(self, instance):
        instance.delete()

