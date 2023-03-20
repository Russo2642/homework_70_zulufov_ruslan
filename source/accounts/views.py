from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import RedirectURLMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView, CreateView

from accounts.forms import LoginForm

from accounts.forms import CustomUserCreationForm


class LoginView(RedirectURLMixin, TemplateView):
    template_name = 'login.html'
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form
        context = {'form': form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, 'Invalid data')
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'User not found')
            return redirect('login')
        login(request, user)
        messages.success(request, 'Welcome!')
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect('index')


def logout_view(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    logout(request)
    return redirect(return_path)


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {'form': form}
        return self.render_to_response(context)
