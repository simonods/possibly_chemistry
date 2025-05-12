from django.contrib import admin
from .models import Lesson, Test, ThematicTag, ThematicRelation

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('thematic_relations', 'tags')
    search_fields = ('title', 'description')


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')
    list_filter = ('thematic_relations', 'tags')
    search_fields = ('title', 'description')


@admin.register(ThematicTag)
class ThematicTagAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(ThematicRelation)
class ThematicRelationAdmin(admin.ModelAdmin):
    search_fields = ['title']
