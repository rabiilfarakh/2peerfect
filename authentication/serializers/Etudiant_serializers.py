#Etudiant_serializers
from rest_framework import serializers
from ..models import Etudiant
from .User_serializers import UserSerializer

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

        user.name = user_data.get('name', user.name)
        user.email = user_data.get('email', user.email)
        if 'password' in user_data:
            user.set_password(user_data['password'])
        user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
    
    def delete(self, instance):
        instance.user.delete()
        instance.delete()
