from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, CreateView

from tracker.forms import IssueForm

from tracker.models import Issue

from tracker.models import Project


class IssueCreateView(CreateView):
    model = Issue
    form_class = IssueForm
    template_name = 'issue/issue_create.html'

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        issue = form.save(commit=False)
        issue.project = project
        issue.save()
        form.save_m2m()
        return redirect('issue_detail', pk=project.pk)


class DetailView(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class UpdateView(TemplateView):
    template_name = 'issue_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        context['form'] = IssueForm(instance=context['issue'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'issue_update.html',
                      context={
                          'form': form,
                          'issue': issue
                      })


class DeleteView(TemplateView):
    template_name = 'issue_confirm_delete.html'

    def get_context_data(self, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        context['form'] = IssueForm(instance=issue)
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('index')
