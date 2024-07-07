import stripe # type: ignore
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from Courses.models import Course
from authentication.models import Etudiant

stripe.api_key = settings.STRIPE_SECRET_KEY

class InitiatePaymentView(APIView):
    def post(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')
        etudiant_id = request.data.get('etudiant_id')
        try:
            course = Course.objects.get(id=course_id)
            etudiant = Etudiant.objects.get(user__id=etudiant_id)
            amount = int(course.prix * 100)  # Convertir le montant en centimes
            payment_intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                metadata={'course_id': course.id, 'etudiant_id': etudiant.user.id}
            )
            payment = Payment.objects.create(
                etudiant=etudiant,
                course=course,
                amount=course.prix,
                status='Pending'
            )
            return Response({
                'paymentIntent': payment_intent,
                'payment': PaymentSerializer(payment).data
            }, status=status.HTTP_201_CREATED)
        except Course.DoesNotExist:
            return Response({"error": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        except Etudiant.DoesNotExist:
            return Response({"error": "Etudiant not found"}, status=status.HTTP_404_NOT_FOUND)

class PaymentStatusView(APIView):
    def get(self, request, *args, **kwargs):
        payment_id = kwargs.get('payment_id')
        try:
            payment = Payment.objects.get(id=payment_id)
            return Response(PaymentSerializer(payment).data)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)

class UpdatePaymentStatusView(APIView):
    def post(self, request, *args, **kwargs):
        payment_id = request.data.get('payment_id')
        try:
            payment = Payment.objects.get(id=payment_id)
            payment_intent_id = request.data.get('payment_intent_id')

            payment_intent = stripe.PaymentIntent.retrieve(payment_intent_id)

            if payment_intent.status == 'succeeded':
                payment.status = 'Completed'
            elif payment_intent.status == 'requires_payment_method':
                payment.status = 'Pending'
            else:
                payment.status = 'Failed'

            payment.save()
            return Response(PaymentSerializer(payment).data, status=status.HTTP_200_OK)
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=status.HTTP_404_NOT_FOUND)
