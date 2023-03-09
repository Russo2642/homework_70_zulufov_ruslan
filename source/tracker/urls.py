from django.urls import path
from tracker.views.base import IndexView, IndexRedirectView
from tracker.views.issues import DetailView, UpdateView, DeleteView

from tracker.views.projects import ProjectDetail

from tracker.views.projects import ProjectCreate

from tracker.views.issues import IssueCreateView

from tracker.views.projects import ProjectUpdate

from tracker.views.projects import ProjectDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/', IndexRedirectView.as_view(), name='issues_redirect'),
    path('project/<int:pk>/issue/add/', IssueCreateView.as_view(), name='issue_add'),
    path('project/issue/<int:pk>', DetailView.as_view(), name='issue_detail'),
    path('project/issue/<int:pk>/update/', UpdateView.as_view(), name='issue_update'),
    path('project/issue/<int:pk>/delete/', DeleteView.as_view(), name='issue_delete'),
    path('project/issue/<int:pk>/confirm_delete/', DeleteView.as_view(), name='confirm_delete'),
    path('project/add/', ProjectCreate.as_view(), name='project_add'),
    path('project/<int:pk>/', ProjectDetail.as_view(), name='project_detail'),
    path('project/<int:pk>/update', ProjectUpdate.as_view(), name='project_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('project/<int:pk>/confirm_delete/', ProjectDeleteView.as_view(), name='project_confirm_delete'),
]
