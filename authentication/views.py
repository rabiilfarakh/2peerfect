from rest_framework.permissions import AllowAny  
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from .models import Professeur, Centre, Etudiant
from .serializers import ProfesseurSerializer, CentreSerializer, EtudiantSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        raise NotImplementedError("Subclasses must implement get_serializer_class method.")

class ProfRegisterView(RegisterView):
    def get_serializer_class(self):
        return ProfesseurSerializer

class CentreRegisterView(RegisterView):
    def get_serializer_class(self):
        return CentreSerializer

class EtudiantRegisterView(RegisterView):
    def get_serializer_class(self):
        return EtudiantSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            
            response_data = {'access': token}
            response_data['message'] = self.get_success_message(user)

            # Stocker le token dans le local storage du navigateur (à gérer côté frontend)

            return Response(response_data)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    def get_success_message(self, user):
        if hasattr(user, 'etudiant'):
            return 'Accès réussi en tant qu\'étudiant'
        elif hasattr(user, 'professeur'):
            return 'Accès réussi en tant que professeur'
        elif hasattr(user, 'centre'):
            return 'Accès réussi en tant que centre'
        else:
            return 'Accès réussi'

class EtudiantLoginView(LoginView):
    pass

class ProfLoginView(LoginView):
    pass

class CentreLoginView(LoginView):
    pass
