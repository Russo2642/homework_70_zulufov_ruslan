from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from tracker.forms import IssueForm

from tracker.models import Issue


class AddView(TemplateView):
    template_name = 'issue_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IssueForm()
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            return redirect('issue_detail', pk=issue.pk)
        return render(request, 'issue_create.html',
                      context={
                          'form': form
                      })


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
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.delete()
        return redirect('index')
