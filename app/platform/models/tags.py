from django.db import models


class ThematicRelation(models.Model):
    """
    Дерево тем: дозволяє темам бути пов’язаними у деревовидну структуру.
    """
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self', null=True, blank=True, related_name='children', on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Тематичний розділ"
        verbose_name_plural = "Тематичні розділи"

    def __str__(self):
        return self.name


class ThematicTag(models.Model):
    """
    Теги тем: дозволяє додавати теги до тем, щоб класифікувати їх за певними критеріями.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = "Тематичний тег"
        verbose_name_plural = "Тематичні теги"

    def __str__(self):
        return self.name