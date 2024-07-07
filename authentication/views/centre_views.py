#centre_views
from rest_framework.permissions import AllowAny
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Centre
from ..serializers.Centre_serializers import CentreSerializer
from .User_views import RegisterView, LoginView

class CentreRegisterView(RegisterView):
    def get_serializer_class(self):
        return CentreSerializer

class CentreDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Centre.objects.all()
    serializer_class = CentreSerializer
    permission_classes = []
    
class CentreLoginView(LoginView):
    pass
