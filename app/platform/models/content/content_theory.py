from django.db import models
from app.platform.models.base import BaseContent
from app.platform.models.lesson_theme import LessonTheme

class TheoryContent(BaseContent):
    """
    Теоретичний матеріал, що входить до складу уроку.
    """
    lesson_theme = models.ForeignKey(
        LessonTheme,
        on_delete=models.CASCADE,
        related_name='theories',
        verbose_name='Тема уроку'
    )
    title = models.CharField(max_length=255, verbose_name='Заголовок блоку теорії')


    class Meta(BaseContent.Meta):
        verbose_name = "Теоретичний матеріал"
        verbose_name_plural = "Теоретичні матеріали"

    def __str__(self):
        return f"{self.lesson_theme} — {self.title}"
