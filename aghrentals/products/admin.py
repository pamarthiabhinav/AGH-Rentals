from django.contrib import admin
from .models import product
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(product)
class productAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'company', 'price', 'category']
    list_display_links = ['name']
    list_filter = ['category', 'company']
    search_fields = ['name', 'company', 'category']
    ordering = ['id']

    class Meta:
        model = product
        fields = ['id', 'name', 'model', 'company', 'category', 'price']
