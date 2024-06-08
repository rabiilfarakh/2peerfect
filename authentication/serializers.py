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

class ProfesseurSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Professeur
        fields = ['user', 'experience', 'cv', 'remote','phone', 'specialty']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        professeur = Professeur.objects.create(user=user, **validated_data)
        return professeur

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

