from django.urls import path
from . import views

urlpatterns = [
    path('', views.Donation.as_view(), name='donate'),
    path('<int:donation_amount>/', views.donationCheckout.as_view(), name='checkout'),
]
