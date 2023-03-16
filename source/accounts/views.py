from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import RedirectURLMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView

from accounts.forms import LoginForm


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
            messages.error(request, 'Некорректные данные')
            return redirect('login')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.error(request, 'Пользователь не найден')
            return redirect('login')
        login(request, user)
        messages.success(request, 'Добро пожаловать')
        next = request.GET.get('next')
        if next:
            return redirect(next)
        return redirect(request.META.get('HTTP_REFERER'))


def logout_view(request):
    return_path = request.META.get('HTTP_REFERER', '/')
    logout(request)
    return redirect(return_path)
