from django.urls import path
from .views import InitiatePaymentView, PaymentStatusView, UpdatePaymentStatusView

urlpatterns = [
    path('initiate/', InitiatePaymentView.as_view(), name='initiate-payment'),
    path('status/<int:payment_id>/', PaymentStatusView.as_view(), name='payment-status'),
    path('update-status/', UpdatePaymentStatusView.as_view(), name='update-payment-status'),
]
