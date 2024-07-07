#etudiant_views
from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from ..models import Etudiant
from ..serializers.Etudiant_serializers import EtudiantSerializer
from .User_views import RegisterView, LoginView

class EtudiantRegisterView(RegisterView):
    def get_serializer_class(self):
        return EtudiantSerializer

class EtudiantLoginView(LoginView):
    pass

class EtudiantDetailView(generics.RetrieveAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

class EtudiantDetailView(generics.RetrieveUpdateDestroyAPIView):
   
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        etudiant = Etudiant.objects.filter(pk=pk).first()
        if etudiant:
            serializer = self.get_serializer(etudiant)
            return Response(serializer.data)
        else:
            return Response({"detail": "No Etudiant matches the given query."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        etudiant = Etudiant.objects.filter(pk=pk).first()
        if etudiant:
            serializer = self.get_serializer(etudiant, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "No Etudiant matches the given query."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        etudiant = Etudiant.objects.filter(pk=pk).first()
        if etudiant:
            etudiant.user.delete()
            etudiant.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "No Etudiant matches the given query."}, status=status.HTTP_404_NOT_FOUND)
