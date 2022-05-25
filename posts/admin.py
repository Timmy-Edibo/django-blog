from django.contrib import admin

# Register your models here.
from . import models
# admin.site.register(Todo)

@admin.register(models.Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['author', 'id', 'title', 'body', 'created_at']
    list_per_page = 10
    search_fields = ['title']