from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Contest(models.Model):
    title = models.CharField(verbose_name='Название', max_length=20)
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(
        verbose_name='Цена',
        help_text='Рекомендованная розничная цена',
        validators=[MinValueValidator(10), MaxValueValidator(100)],
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
    )