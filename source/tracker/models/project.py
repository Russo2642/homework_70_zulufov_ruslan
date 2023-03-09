from django.db import models
from django.utils import timezone


class Project(models.Model):
    start_date = models.DateField(
        null=False,
        verbose_name='Дата начала'
    )
    end_date = models.DateField(
        null=True,
        verbose_name='Дата окончания'
    )
    title = models.CharField(
        max_length=300,
        null=False,
        blank=False,
        verbose_name='Название'
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        verbose_name='Описание'
    )
    is_deleted = models.BooleanField(
        verbose_name='Удалено',
        null=False,
        default=False
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    deleted_at = models.DateTimeField(
        verbose_name="Дата и время удаления",
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.title} - {self.start_date}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()
