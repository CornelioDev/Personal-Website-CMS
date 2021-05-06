from django.contrib import admin
from pages.models import Page

# Customization
class PageAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at')
    ordering = ('-created_at',)
# Register your models here.
admin.site.register(Page, PageAdmin)
