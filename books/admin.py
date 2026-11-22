from django.contrib import admin
from .models import Book, Chapter, Purchase

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'price', 'status', 'created_at')
    list_filter = ('status', 'category')
    list_editable = ('status',)
    inlines = [ChapterInline]

admin.site.register(Purchase)
