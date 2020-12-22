from django.contrib import admin
from blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'published_date']

admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
