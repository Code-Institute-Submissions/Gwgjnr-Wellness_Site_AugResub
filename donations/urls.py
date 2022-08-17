from django.urls import path
from . import views

urlpatterns = [
    path('', views.Donation.as_view(), name='donate'),
    path('checkout/', views.donationCheckout.as_view(), name='checkout'),
]
