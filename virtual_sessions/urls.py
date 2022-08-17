from django.urls import path
from . import views

urlpatterns = [
    path('', views.seminar_search_page, name='seminars'),
    path('<slug:slug>', views.seminar_detail, name='seminar_detail'),
    path('join/<str:title>', views.JoinSeminar.as_view(), name='join_seminar'),
    path('delete/<str:title>', views.DeleteSeminar.as_view(), name='delete_seminar'),
    path('EditComment/<slug:pk>/', views.EditComment.as_view(), name='editcomment'),
    path('deleteComment/<slug:pk>/', views.DeleteOwnComment.as_view(), name='delete_comment'),
]
