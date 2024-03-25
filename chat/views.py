from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'home.html'

class ChatRoomView(TemplateView):
    template_name = 'chat/chat_room.html'

class RegistrationView(TemplateView):
    template_name = 'registration/registration.html'

class LoginView(TemplateView):
    template_name = 'login/login.html'