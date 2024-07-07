#Prof_serializers
from rest_framework import serializers
from ..models import Professeur
from .User_serializers import UserSerializer

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
        instance.user.delete()  # Supprime également l'utilisateur associé
        instance.delete()