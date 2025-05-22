from django.db import models

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class BaseContent(TimeStampedModel):
    """
    Абстрактна базова модель для всіх компонентів уроку: теорія, завдання, тести тощо.
    """
    title = models.CharField(max_length=255, verbose_name='Назва')
    content = models.TextField(verbose_name='Зміст (HTML або текст)')
    order = models.PositiveIntegerField(default=0, verbose_name='Порядок')

    class Meta:
        abstract = True
        ordering = ['order','created_at']

    def __str__(self):
        return self.title

class Difficulty(models.TextChoices):
    EASY = 'easy', 'Легко'
    MEDIUM = 'medium', 'Середня'
    HARD = 'hard', 'Складно'