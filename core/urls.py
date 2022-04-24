from django.urls import path, include
from core import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('home/', views.HomepageView.as_view(), name='home')
]
