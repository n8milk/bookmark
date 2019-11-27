from django.contrib import admin

from .models import Bookmark

class BoomarkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,       {'fields': ['site_name']}),
        ('URL 주소', {'fields': ['url']}),
    ]

    search_fields = ['site_name', 'url']
    # list_display = ('site_name', 'url')
    # list_filter = []

admin.site.register(Bookmark, BoomarkAdmin)
