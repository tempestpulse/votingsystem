from django.contrib.auth import login, logout , authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib import messages
import urllib.request
import json
import urllib.parse

from account.forms import CustomUserCreationForm

class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('election:election-list')


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('election:election-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterView, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('election:election-list')
        return super(RegisterView, self).get(*args, **kwargs)


def logout_view(request):
    logout(request)
    return redirect('election:election-list')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        recaptcha_response = request.POST.get('g-recaptcha-response')
        
        # Weryfikacja reCAPTCHA po stronie serwera
        if recaptcha_response:
            data = urllib.parse.urlencode({
                'secret': '6LdhNMkpAAAAAKoZPOLWvlHJxpCSXurkjwIacyhj',
                'response': recaptcha_response
            }).encode('utf-8')
            req = urllib.request.Request('https://www.google.com/recaptcha/api/siteverify', data=data)
            response = urllib.request.urlopen(req)
            result = json.loads(response.read())

            if result['success']:
                # Jeśli reCAPTCHA została zweryfikowana, wykonaj autentykację użytkownika
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('election:election-list')
                else:
                    messages.error(request, "Invalid username or password. Please try again.")
            else:
                # Jeśli reCAPTCHA nie została zweryfikowana, wyświetl błąd
                messages.error(request, "Please complete the reCAPTCHA.")
        else:
            # Jeśli reCAPTCHA nie została przesłana, wyświetl błąd
            messages.error(request, "Please complete the reCAPTCHA.")
        
    # Jeśli nie jest to metoda POST lub uwierzytelnianie się nie powiodło, renderuj szablon logowania z błędem.
    return render(request, 'account/login.html')
