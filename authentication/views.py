# views.py
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
    expected_role = None  

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        
        if user is not None:
            if self.expected_role and user.role != self.expected_role:
                return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)

            response_data = {
                'access': access_token,
                'refresh': refresh_token,
                'role': user.role 
            }

            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class EtudiantLoginView(LoginView):
    expected_role = 'etudiant' 

class ProfLoginView(LoginView):
    expected_role = 'professeur'  

class CentreLoginView(LoginView):
    expected_role = 'centre'  