from django.urls import path
from django.contrib.auth.views import LogoutView
from core import views

urlpatterns = [
    path('', views.LoginView.as_view(), name='home'),  # redirects to send/ if auth
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('add-belayer/', views.AddBelayerView.as_view(), name='add_belayer'),
    path('remove-belayer/<pk>', views.RemoveBelayerView.as_view(), name='remove_belayer'),
    path('send/', views.MessagingView.as_view(), name='send_message'),
    path('sent/', views.MessageSentView.as_view(), name='message_sent'),
]

