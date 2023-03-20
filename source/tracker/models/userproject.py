from django.contrib.auth.models import User
from django.db import models

from tracker.models import Project


class UserProject(models.Model):
    user = models.ForeignKey(
        to=User,
        related_name='userproject_project',
        verbose_name='Пользователь',
        on_delete=models.CASCADE
    )
    project = models.ForeignKey(
        to=Project,
        related_name='userproject_users',
        verbose_name='Проект',
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Проект пользователя'
        verbose_name_plural = 'Проекты пользователя'
