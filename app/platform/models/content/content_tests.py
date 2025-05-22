from django.db import models
from app.platform.models.lesson_theme import LessonTheme
from app.platform.models.base import BaseContent, Difficulty


class Test(BaseContent):
    """
    Тест, який містить запитання, прив'язаний до теми уроку.
    """
    lesson_theme = models.ForeignKey(
        LessonTheme,
        related_name='tests',
        on_delete=models.CASCADE,
        verbose_name='Тема уроку'
    )
    difficulty = models.CharField(
        max_length=10,
        choices=Difficulty.choices,
        default=Difficulty.MEDIUM,
        verbose_name='Рівень складності тесту'
    )
    total_questions = models.PositiveIntegerField(
        default=0,
        verbose_name='Кількість запитань'
    )
    passing_score = models.PositiveIntegerField(
        default=60,
        verbose_name='Прохідний бал'
    )

    class Meta(BaseContent.Meta):
        verbose_name = "Тест"
        verbose_name_plural = "Тести"

    def __str__(self):
        return f"{self.lesson_theme} — {self.title}"
