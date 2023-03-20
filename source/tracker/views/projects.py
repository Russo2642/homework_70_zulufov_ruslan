from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from tracker.forms import ProjectForm
from tracker.forms import UserProjectForm
from tracker.models import Project

from tracker.models import UserProject


class GroupPermissionMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name__in=['admin', 'Project Manager', 'Team Lead', 'Developer']).exists()


class ProjectCreate(GroupPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, CreateView):
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


class ProjectUpdate(GroupPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'project/project_update.html'
    model = Project
    form_class = ProjectForm
    success_message = 'Проект обновлён'
    groups = ['admin', 'Project Manager']

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(GroupPermissionMixin, SuccessMessageMixin, LoginRequiredMixin, DeleteView):
    template_name = 'project/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')
    success_message = 'Проект удалён'
    groups = ['admin', 'Project Manager']


class UserProjectCreateView(GroupPermissionMixin, LoginRequiredMixin, UpdateView):
    model = Project
    form_class = UserProjectForm
    template_name = 'project/userproject_create.html'
    groups = ['admin', 'Project Manager', 'Team Lead']

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})
