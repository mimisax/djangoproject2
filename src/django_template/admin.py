from django.contrib import admin
from .models import BookStore

# Register your models here.

class BookStoreDB(admin.ModelAdmin):
    list_display = [
        "book_title", "book_author", "year_published"
    ]


admin.site.register(BookStore, BookStoreDB)

from django.contrib import admin
from .models import  Comment
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)