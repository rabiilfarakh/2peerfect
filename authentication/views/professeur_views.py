#professeur_views
from rest_framework.permissions import AllowAny
from rest_framework import generics
from ..models import Professeur
from ..serializers.Prof_serializers import ProfesseurSerializer
from .User_views import RegisterView, LoginView

class ProfRegisterView(RegisterView):
    def get_serializer_class(self):
        return ProfesseurSerializer


class ProfLoginView(LoginView):
    pass

class ProfesseurDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Professeur.objects.all()
    serializer_class = ProfesseurSerializer
    permission_classes = []
