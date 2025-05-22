from django.db import models
from .base import TimeStampedModel
from .stage import StudyStage
from .tags import ThematicTag, ThematicRelation
from django.utils.text import slugify


class StudyTheme(TimeStampedModel):
    """
    Модель для навчальних тем в рамках етапу навчання.
    """
    stage = models.ForeignKey(
        StudyStage,
        on_delete=models.CASCADE,
        related_name="themes",
        verbose_name="Навчальний етап"
    )
    title = models.CharField(max_length=255, verbose_name="Назва теми")
    slug = models.SlugField(max_length=255, db_index=True, verbose_name="Slug")
    description = models.TextField(blank=True, verbose_name="Опис")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок теми")

    tags = models.ManyToManyField(
        ThematicTag,
        blank=True,
        verbose_name="Теги теми"
    )
    thematic_relations = models.ManyToManyField(
        ThematicRelation,
        blank=True,
        related_name="studytheme_thematic_relations",
        verbose_name="Тематичні зв’язки"
    )

    class Meta:
        verbose_name = "Навчальна тема"
        verbose_name_plural = "Навчальні теми"
        ordering = ['order', 'name']
        unique_together = ['stage', 'slug']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.stage.name} — {self.title}"
