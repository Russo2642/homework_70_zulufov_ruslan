from django.db.models import Q
from django.urls import reverse, reverse_lazy
from django.utils.http import urlencode
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from tracker.forms import ProjectForm, SearchForm
from tracker.models import Project

from tracker.models import Issue


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
    # paginate_by = 10
    # paginate_orphans = 1


    # def get(self, request, *args, **kwargs):
    #     self.form = self.get_search_form()
    #     self.search_value = self.get_search_value()
    #     return super().get(request, *args, **kwargs)
    #
    # def get_search_form(self):
    #     return SearchForm(self.request.GET)
    #
    # def get_search_value(self):
    #     if self.form.is_valid():
    #         return self.form.cleaned_data['search']
    #     return None
    #
    # def get_queryset(self):
    #     queryset = super().get_queryset().exclude(is_deleted=True)
    #     if self.search_value:
    #         query = Q(summary__icontains=self.search_value) | Q(description__icontains=self.search_value)
    #         queryset = queryset.filter(query)
    #     return queryset
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(object_list=object_list, **kwargs)
    #     context['form'] = self.form
    #     if self.search_value:
    #         context['query'] = urlencode({'search': self.search_value})
    #     return context


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
