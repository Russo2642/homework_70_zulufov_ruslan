from django import forms

from tracker.models import Issue


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['summary', 'description', 'status', 'type']
        labels = {
            'summary': 'Summary',
            'description': 'Description',
            'status': 'Status',
            'type': 'Type'
        }
