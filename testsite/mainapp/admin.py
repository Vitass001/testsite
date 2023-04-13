from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'content',)
    # list_filter = ('update', 'timestamp')
    # list_editable = ('title', )
    # list_display_links = ('update', )

admin.site.register(Post)


