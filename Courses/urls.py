# courses/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, QuizViewSet, QuestionViewSet, TakeQuizView, CertificateViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='course')
router.register(r'quizzes', QuizViewSet, basename='quiz')
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'certificates', CertificateViewSet, basename='certificate')

urlpatterns = [
    path('', include(router.urls)),
    path('quiz/take/', TakeQuizView.as_view(), name='take_quiz'),
]

# Avec cette configuration, vos API endpoints seront :

# Courses:
# POST /api/courses/ pour créer un nouveau cours.
# GET /api/courses/ pour lister tous les cours.
# GET /api/courses/<int:pk>/ pour récupérer un cours spécifique.
# PUT /api/courses/<int:pk>/ pour mettre à jour un cours spécifique.
# PATCH /api/courses/<int:pk>/ pour mettre à jour partiellement un cours spécifique.
# DELETE /api/courses/<int:pk>/ pour supprimer un cours spécifique.

# Quizzes:
# POST /api/quizzes/ pour créer un nouveau quiz.
# GET /api/quizzes/ pour lister tous les quizzes.
# GET /api/quizzes/<int:pk>/ pour récupérer un quiz spécifique.
# PUT /api/quizzes/<int:pk>/ pour mettre à jour un quiz spécifique.
# PATCH /api/quizzes/<int:pk>/ pour mettre à jour partiellement un quiz spécifique.
# DELETE /api/quizzes/<int:pk>/ pour supprimer un quiz spécifique.

# Questions:
# POST /api/questions/ pour créer une nouvelle question.
# GET /api/questions/ pour lister toutes les questions.
# GET /api/questions/<int:pk>/ pour récupérer une question spécifique.
# PUT /api/questions/<int:pk>/ pour mettre à jour une question spécifique.
# PATCH /api/questions/<int:pk>/ pour mettre à jour partiellement une question spécifique.
# DELETE /api/questions/<int:pk>/ pour supprimer une question spécifique.

# Certificates:
# GET /api/certificates/ pour lister tous les certificats.
# GET /api/certificates/<int:pk>/ pour récupérer un certificat spécifique.

# Take Quiz:
# POST /api/quiz/take/ pour permettre à un étudiant de passer un quiz et obtenir un certificat s'il réussit.