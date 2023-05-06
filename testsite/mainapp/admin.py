from django.contrib import admin
from .models import Post, Property, Legal


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'content',)
    # list_filter = ('update', 'timestamp')
    # list_editable = ('title', )
    # list_display_links = ('update', )

admin.site.register(Post)


class PropertyAdmin(admin.ModelAdmin):
    list_display = ('company',  'property',)
    # list_filter = ('update', 'timestamp')
    # list_editable = ('title', )
    # list_display_links = ('update', )

admin.site.register(Property)


class LegalAdmin(admin.ModelAdmin):
    list_display = ('Legal_Entity')
    # list_filter = ('update', 'timestamp')
    # list_editable = ('title', )
    # list_display_links = ('update', )

admin.site.register(Legal)