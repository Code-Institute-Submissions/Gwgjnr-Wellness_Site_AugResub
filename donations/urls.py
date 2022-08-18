from django.urls import path
from . import views

urlpatterns = [
    path('', views.Donation.as_view(), name='donate'),
    path('checkout/', views.DonationCheckout.as_view(), name='checkout'),
]
