from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')

    list_filter = ('created_at',)

    search_fields = ('title', 'author__username')

    fields = ('title', 'text', 'image', 'author')

    ordering = ('-created_at',)

    def author(self, obj):
        return obj.author.username

    author.short_description = 'Author'


admin.site.register(Post, PostAdmin)
