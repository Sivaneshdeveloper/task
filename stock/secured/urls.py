from django.urls import path
from .views import StudentView,stock

urlpatterns = [
    path('users/', StudentView.as_view()),
path('students/<int:pk>/', StudentView.as_view()),
    path('stocks/',stock)
]