from django import forms
from django.forms import widgets
from tracker.models import Issue

from tracker.models.validators.validator import tracker_summary_validator, tracker_description_validator


class IssueForm(forms.ModelForm):
    summary = forms.CharField(
        validators=[
            tracker_summary_validator
        ]
    )
    description = forms.CharField(
        validators=[
            tracker_description_validator
        ],
        widget=widgets.Textarea()
    )

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
            'types': forms.CheckboxSelectMultiple,
        }
