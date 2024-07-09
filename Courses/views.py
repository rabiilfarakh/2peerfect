# courses/views.py
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Course, Quiz, Question, Certificate
from .serializers import CourseSerializer, QuizSerializer, QuestionSerializer, CertificateSerializer
from authentication.models import Etudiant
from .utils import create_certificate_image

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class TakeQuizView(APIView):
    def post(self, request, *args, **kwargs):
        quiz_id = request.data.get('quiz_id')
        student_id = request.data.get('student_id')
        answers = request.data.get('answers')
        try:
            quiz = Quiz.objects.get(id=quiz_id)
            student = Etudiant.objects.get(user__id=student_id)
            correct_count = 0
            for question_id, answer in answers.items():
                question = Question.objects.get(id=question_id, quiz=quiz)
                if question.correct_answer == answer:
                    correct_count += 1
            # Assume 70% correct answers required to pass
            if correct_count / quiz.question_set.count() >= 0.7:
                certificate = Certificate.objects.create(
                    student=student,
                    course=quiz.course,
                    certificate_image=create_certificate_image(student, quiz.course)
                )
                return Response({"message": "Quiz passed!", "certificate": CertificateSerializer(certificate).data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Quiz failed."}, status=status.HTTP_400_BAD_REQUEST)
        except Quiz.DoesNotExist:
            return Response({"error": "Quiz not found"}, status=status.HTTP_404_NOT_FOUND)
        except Etudiant.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

class CertificateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
