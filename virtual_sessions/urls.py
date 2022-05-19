from django.urls import path
from . import views

urlpatterns = [
    path('', views.seminar_search_page, name='seminars'),
    path('<session_id>', views.seminar_detail, name='seminar_detail'),
    path('join/<str:title>', views.JoinSeminar.as_view(), name='join_seminar'),
    path('delete/<str:title>', views.DeleteSeminar.as_view(), name='delete_seminar'),
]
