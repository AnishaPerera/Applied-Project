from django.contrib import admin
from .models import Thread, Comment, Reply

# Register your models here.

class CommentInline(admin.StackedInline):
    model = Comment

class ReplyInline(admin.StackedInline):
    model = Reply

class ThreadAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display=['title', 'author', 'content', 'creation']

class CommentAdmin(admin.ModelAdmin):
    inlines = [ReplyInline]
    list_display = ['thread_id', 'author', 'content', 'creation']

admin.site.register(Thread,ThreadAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Reply)