from django import forms

from tracker.models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'types']
        labels = {
            'summary': 'Summary',
            'description': 'Description',
            'status': 'Status',
            'types': 'Type'
        }
        widgets = {
            'status': forms.RadioSelect,
            'types': forms.CheckboxSelectMultiple
        }
