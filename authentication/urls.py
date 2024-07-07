from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views.User_views import UserDetailView, LoginView, RegisterView
from .views.professeur_views import ProfesseurDetailView, ProfRegisterView, ProfLoginView
from .views.centre_views import CentreDetailView, CentreRegisterView, CentreLoginView
from .views.etudiant_views import EtudiantDetailView, EtudiantRegisterView, EtudiantLoginView

urlpatterns = [
    #Professeur
    path('register/prof/', ProfRegisterView.as_view(), name='register_professeur'),
    path('login/prof/', ProfLoginView.as_view(), name='login_prof'),
    path('professeurs/<int:pk>/', ProfesseurDetailView.as_view(), name='professeur_detail'),
    
    
    path('register/centre/', CentreRegisterView.as_view(), name='register_centre'),
    path('centres/<int:pk>/', CentreDetailView.as_view(), name='centre_detail'),
    path('login/centre/', CentreLoginView.as_view(), name='login_centre'),
    
    #Etudiant
    path('register/etudiant/', EtudiantRegisterView.as_view(), name='register_etudiant'),
    path('etudiant/<int:pk>/', EtudiantDetailView.as_view(), name='etudiant-detail'),
    path('login/etudiant/', EtudiantLoginView.as_view(), name='login_etudiant'),
    
#     path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    

     
 ]
