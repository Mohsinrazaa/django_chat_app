from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model
User = get_user_model()
class HomeView(TemplateView):
    template_name = 'home.html'

class ChatRoomView(TemplateView):
    template_name = 'chat/chat_room.html'

class RegistrationView(TemplateView):
    template_name = 'registration/registration.html'

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            # Authenticate against the correct user model
            user = authenticate(request, username=username, password=raw_password)
            login(request, user)
            return redirect('home')  # Redirect to home page after successful registration
        return render(request, self.template_name, {'form': form})

class LoginView(TemplateView):
    template_name = 'login/login.html'

    def get(self, request):
        form = AuthenticationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to home page after successful login
        return render(request, self.template_name, {'form': form})
class PasswordResetView(TemplateView):
    template_name = 'password_reset/password_reset.html'

    def get(self, request):
        return render(request, self.template_name)