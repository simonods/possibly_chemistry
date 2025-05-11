from django.db import models

# from .base import TimeStampedModel
from .tags import ThematicTag, ThematicRelation

class ContentBase(models.Model):
    """
    Абстрактна модель, яку успадковують всі типи навчального контенту.
    """
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    tags = models.ManyToManyField(ThematicTag, blank=True)
    thematic_relations = models.ManyToManyField(ThematicRelation, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Lesson(ContentBase):
    content = models.TextField(help_text="Основний текст або HTML-контент уроку.")
    video_url = models.URLField(blank=True, help_text="Посилання на відео з хмари (YouTube, Vimeo, тощо)")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"


class Theory(ContentBase):
    content = models.TextField()

    class Meta:
        verbose_name = "Теоретична частина"
        verbose_name_plural = "Теоретичні частини"


class Test(ContentBase):
    total_questions = models.PositiveIntegerField(default=0)
    passing_score = models.PositiveIntegerField(default=60)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тести"
