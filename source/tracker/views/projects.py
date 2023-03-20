from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from tracker.forms import ProjectForm
from tracker.models import Project
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from tracker.forms import UserProjectForm


class ProjectCreate(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Проект создан'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'project/project.html'
    model = Project
    ordering = ('-created_at',)


class ProjectUpdate(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'project/project_update.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Проект обновлён'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'project/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')
    success_message = 'Проект удалён'


class UserProjectCreateView(LoginRequiredMixin, UpdateView):
    model = Project
    form_class = UserProjectForm
    template_name = 'project/userproject_create.html'

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
