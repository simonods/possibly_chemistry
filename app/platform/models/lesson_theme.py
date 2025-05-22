from django.db import models
from .base import TimeStampedModel
from .study_theme import StudyTheme
from .tags import ThematicTag, ThematicRelation
from django.utils.text import slugify


class LessonTheme(TimeStampedModel):
    study_theme = models.ForeignKey(
        StudyTheme,
        on_delete=models.CASCADE,
        related_name='lessons',
        verbose_name='Навчальна тема'
    )
    title = models.CharField(max_length=255, verbose_name='Назва теми уроку')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Опис")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок уроку")

    tags = models.ManyToManyField(
        ThematicTag,
        blank=True,
        related_name='lesson_theme_tags',
        verbose_name="Теги уроку"
    )
    thematic_relations = models.ManyToManyField(
        ThematicRelation,
        blank=True,
        related_name="lessontheme_thematic_relations",
        verbose_name="Тематичні зв’язки"
    )

    class Meta:
        verbose_name = "Тема уроку"
        verbose_name_plural = "Теми уроків"
        ordering = ['order', 'title']
        unique_together = ['study_theme', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.study_theme.name} — {self.title}"
