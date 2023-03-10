from django.db import models


class Issue(models.Model):
    summary = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name='Заголовок'
    )
    description = models.TextField(
        max_length=3000,
        null=True,
        verbose_name="Полное описание"
    )
    status = models.ForeignKey(
        'tracker.Status',
        related_name='issue',
        on_delete=models.PROTECT,
        verbose_name='Статус'
    )
    types = models.ManyToManyField(
        'tracker.Type',
        related_name='issue'
    )
    project = models.ForeignKey(
        'tracker.Project',
        related_name='issue',
        on_delete=models.PROTECT,
        verbose_name='Проект'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )

    def __str__(self):
        return f"{self.summary} - {self.status}"

    def get_types(self):
        return "\n".join([t.name for t in self.types.all()])

    get_types.short_description = "Тип"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
