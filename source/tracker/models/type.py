from django.db import models


class Type(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Наименование')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
