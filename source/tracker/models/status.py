from django.db import models


class Status(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Статус')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
