# auth/urls.py
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import ProfRegisterView, CentreRegisterView, EtudiantRegisterView, LoginView, EtudiantLoginView, ProfLoginView, CentreLoginView

urlpatterns = [
    path('register/prof/', ProfRegisterView.as_view(), name='register_professeur'),
    path('register/centre/', CentreRegisterView.as_view(), name='register_centre'),
    path('register/etudiant/', EtudiantRegisterView.as_view(), name='register_etudiant'),
    path('login/', LoginView.as_view(), name='login'),
    path('login/etudiant/', EtudiantLoginView.as_view(), name='login_etudiant'),
    path('login/prof/', ProfLoginView.as_view(), name='login_prof'),
    path('login/centre/', CentreLoginView.as_view(), name='login_centre'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
