from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import About, Comment, Post, Policy, Contact


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post)
admin.site.register(About)
admin.site.register(Policy)
admin.site.register(Contact)