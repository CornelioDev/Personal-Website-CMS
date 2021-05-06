from django.contrib import admin
from blog.models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'updated_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'user', 'public', 'created_at')
    list_filter = ('public', 'categories__name', 'user__username')

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)