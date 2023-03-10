from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView
from tracker.forms import ProjectForm
from tracker.models import Project


class ProjectCreate(CreateView):
    template_name = 'project/project_create.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDetail(DetailView):
    template_name = 'project/project.html'
    model = Project
    ordering = ('-created_at',)


class ProjectUpdate(UpdateView):
    template_name = 'project/project_update.html'
    model = Project
    form_class = ProjectForm

    def get_success_url(self):
        return reverse('project_detail', kwargs={'pk': self.object.pk})


class ProjectDeleteView(DeleteView):
    template_name = 'project/project_confirm_delete.html'
    model = Project
    success_url = reverse_lazy('index')
