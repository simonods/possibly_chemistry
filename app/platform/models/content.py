from django.db import models

from .base import TimeStampedModel
from .tags import ThematicTag, ThematicRelation

class ContentBase(TimeStampedModel):
    """
    Абстрактна модель, яку успадковують всі типи навчального контенту.
    """
    title = models.CharField(max_length=255, verbose_name='Назва')
    description = models.TextField(blank=True, verbose_name='Опис')
    tags = models.ManyToManyField(ThematicTag, blank=True, verbose_name='Теги теми')
    thematic_relations = models.ManyToManyField(
        ThematicRelation,
        blank=True,
        verbose_name='Причасність до теми',
        related_name="%(class)s_thematic_relations"
    )

    class Meta:
        abstract = True
        ordering = ['-created_at', 'updated_at', 'title']

    def __str__(self):
        return self.title


class Lesson(ContentBase):
    content = models.TextField(help_text="Основний текст або HTML-контент уроку.", verbose_name='Урок текст')
    video_url = models.URLField(blank=True, help_text="Посилання на відео з хмари (YouTube, Vimeo, тощо)", verbose_name='Посилання на відео')

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"



class Test(ContentBase):
    total_questions = models.PositiveIntegerField(default=0)
    passing_score = models.PositiveIntegerField(default=60)

    class Meta:
        verbose_name = "Тест"
        verbose_name_plural = "Тести"
