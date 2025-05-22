from django.db import models
from .base import TimeStampedModel
from django.utils.text import slugify


class Subject(TimeStampedModel):
    """
    Модель для предметів, які викладаються в курсах.
    """
    title = models.CharField(max_length=255, unique=True, verbose_name="Назва предмету")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="Slug")

    class Meta:
        verbose_name = "Предмет"
        verbose_name_plural = "Предмети"
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
