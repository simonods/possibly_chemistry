from django.db import models
from app.platform.models.base import BaseContent
from app.platform.models.lesson_theme import LessonTheme


class TeacherMaterial(BaseContent):
    """
    Матеріали для вчителя, прив’язані до конкретної теми уроку.
    """
    lesson_theme = models.ForeignKey(
        LessonTheme,
        on_delete=models.CASCADE,
        related_name='teacher_materials',
        verbose_name='Тема уроку'
    )

    class Meta(BaseContent.Meta):
        verbose_name = "Матеріал для вчителя"
        verbose_name_plural = "Матеріали для вчителя"

    def __str__(self):
        return f"{self.lesson_theme} — {self.title}"
