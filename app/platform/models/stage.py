from django.db import models
from .base import TimeStampedModel
from .subject import Subject
from django.utils.text import slugify


class StudyStage(TimeStampedModel):
    """
    Модель для етапів навчання в рамках предмету.
    """
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
        related_name="stages",
        verbose_name="Предмет"
    )
    title = models.CharField(max_length=255, verbose_name="Назва етапу")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="Slug")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок відображення")

    class Meta:
        verbose_name = "Етап навчання"
        verbose_name_plural = "Етапи навчання"
        ordering = ['order', 'title']
        unique_together = ['subject', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject.name} – {self.title}"
