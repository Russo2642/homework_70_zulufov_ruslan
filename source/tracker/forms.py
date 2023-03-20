from django import forms
from django.contrib.auth.models import User
from django.forms import widgets
from tracker.models import Issue
from tracker.models import Project
from tracker.models.validators.validator import tracker_summary_validator, tracker_description_validator

from tracker.models import UserProject


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


class ProjectForm(forms.ModelForm):
    start_date = forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=widgets.DateInput(attrs={'type': 'date'}), required=False)

    class Meta:
        model = Project
        fields = ['title', 'description', 'start_date', 'end_date']
        labels = {
            'title': 'Title',
            'description': 'Description',
            'start_date': 'Start Date',
            'end_date': 'End Date',
        }


class SearchForm(forms.Form):
    search = forms.CharField(max_length=20, required=False, label='Search')


class UserProjectForm(forms.ModelForm):
    # users = forms.CharField(label='User', widget=forms.CheckboxSelectMultiple)
    # class Meta:
    #     model = Project
    #     fields = ['users']
    #     labels = {
    #         'users': 'User'
    #     }
    class Meta:
        model = Project
        fields = ['users']
        labels = {
            'users': 'User'
        }
        widgets = {
            'users': forms.CheckboxSelectMultiple
        }
