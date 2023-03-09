from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from tracker.forms import IssueForm
from tracker.models import Issue


class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue/issue_create.html'

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueDetailView(DetailView):
    template_name = 'issue/issue.html'
    model = Issue


class IssueUpdateView(UpdateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue/issue_update.html'

    def get_success_url(self):
        return reverse('issue_detail', kwargs={'pk': self.object.pk})


class IssueDeleteView(DeleteView):
    template_name = 'issue/issue_confirm_delete.html'
    model = Issue
    success_url = reverse_lazy('index')
