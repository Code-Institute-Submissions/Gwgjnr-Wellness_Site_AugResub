from django.urls import path
from . import views

urlpatterns = [
    path('', views.seminar_search_page, name='seminars'),
    path('<session_id>', views.seminar_detail, name='seminar_detail'),
]
