from django.db import models

from app.platform.models.base import BaseContent, Difficulty
from app.platform.models.lesson_theme import LessonTheme


class TaskBase(BaseContent):
    """
    Базова модель для завдань (звичайних та преміум).
    """
    lesson_theme = models.ForeignKey(
        LessonTheme,
        on_delete=models.CASCADE,
        related_name="%(class)ss",
        verbose_name="Тема уроку"
    )

    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.MEDIUM,
        verbose_name="Складність"
    )

    # Під питанням для подальшої більш тонкого налаштування
    # order = models.PositiveIntegerField(
    #     default=0,
    #     verbose_name="Порядок",
    #     help_text="Використовується для сортування завдань у межах теми."
    # )

    class Meta:
        abstract = True
        ordering = ['order']


class Task(TaskBase):
    class Meta:
        verbose_name = "Завдання"
        verbose_name_plural = "Завдання"

    def __str__(self):
        return f"Завдання #{self.pk} ({self.difficulty})"


class PremiumTask(TaskBase):
    class Meta:
        verbose_name = "Преміум-завдання"
        verbose_name_plural = "Преміум-завдання"

    def __str__(self):
        return f"Преміум-завдання #{self.pk} ({self.difficulty})"
