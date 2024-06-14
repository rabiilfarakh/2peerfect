from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import Professeur, Centre, Etudiant, User
from .serializers import ProfesseurSerializer, CentreSerializer, EtudiantSerializer, UserSerializer

# Classe de base pour les vues d'inscription
class RegisterView(APIView):
    # Autorise tout le monde à accéder à cette vue
    permission_classes = [AllowAny]

    # Méthode POST pour créer un nouvel utilisateur
    def post(self, request):
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Méthode pour obtenir la classe du sérialiseur, à implémenter par les sous-classes
    def get_serializer_class(self):
        raise NotImplementedError("Subclasses must implement get_serializer_class method.")

# Vue pour l'inscription des professeurs
class ProfRegisterView(RegisterView):
    # Retourne le sérialiseur du professeur
    def get_serializer_class(self):
        return ProfesseurSerializer

# Vue pour l'inscription des centres
class CentreRegisterView(RegisterView):
    # Retourne le sérialiseur du centre
    def get_serializer_class(self):
        return CentreSerializer

# Vue pour l'inscription des étudiants
class EtudiantRegisterView(RegisterView):
    # Retourne le sérialiseur de l'étudiant
    def get_serializer_class(self):
        return EtudiantSerializer

# Vue pour la connexion des utilisateurs
class LoginView(APIView):
    # Autorise tout le monde à accéder à cette vue
    permission_classes = [AllowAny]

    # Méthode POST pour authentifier un utilisateur
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            
            response_data = {'access': token}
            response_data['message'] = self.get_success_message(user)

            return Response(response_data)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    # Méthode pour obtenir un message de succès personnalisé en fonction du type d'utilisateur
    def get_success_message(self, user):
        if hasattr(user, 'etudiant'):
            return 'Accès réussi en tant qu\'étudiant'
        elif hasattr(user, 'professeur'):
            return 'Accès réussi en tant que professeur'
        elif hasattr(user, 'centre'):
            return 'Accès réussi en tant que centre'
        else:
            return 'Accès réussi'

# Vue pour la connexion des étudiants
class EtudiantLoginView(LoginView):
    pass

# Vue pour la connexion des professeurs
class ProfLoginView(LoginView):
    pass

# Vue pour la connexion des centres
class CentreLoginView(LoginView):
    pass


# Vue pour les opérations CRUD sur les utilisateurs
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []

# Vue pour les opérations CRUD sur les professeurs
class ProfesseurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer
    permission_classes = [] 

# Vue pour les opérations CRUD sur les centres
class CentreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer
    permission_classes = []

# Vue pour les opérations CRUD sur les étudiants
class EtudiantDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    permission_classes = []
