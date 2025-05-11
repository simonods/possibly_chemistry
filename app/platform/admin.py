from django.contrib import admin
from .models.tags import ThematicTag, ThematicRelation
from .models.content import Lesson, Test, Theory

admin.site.register(ThematicTag)
admin.site.register(ThematicRelation)
admin.site.register(Lesson)
admin.site.register(Theory)
admin.site.register(Test)
