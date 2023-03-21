from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from tracker.forms import ProjectForm
from tracker.forms import UserProjectForm
from tracker.models import Project


class ManagerGroupPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'Project Manager']).exists()


class ProjectCreate(ManagerGroupPermissionMixin, SuccessMessageMixin, CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Проект создан'
    groups = ['admin', 'Project Manager']

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'project/project.html'
    model = Project
    ordering = ('-created_at',)


class ProjectUpdate(UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    template_name = 'project/project_update.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Проект обновлён'
    groups = ['admin', 'Project Manager']

    def test_func(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        for user in project.users.all():
            return user == self.request.user and self.request.user.has_perm('tracker.change_project')

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    template_name = 'project/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')
    success_message = 'Проект удалён'

    def test_func(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        for user in project.users.all():
            return user == self.request.user and self.request.user.has_perm('tracker.delete_project')


class UserProjectCreateView(UserPassesTestMixin, UpdateView):
    model = Project
    form_class = UserProjectForm
    template_name = 'project/userproject_create.html'

    def test_func(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        for user in project.users.all():
            return user == self.request.user and self.request.user.has_perm('tracker.add_userproject')

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
