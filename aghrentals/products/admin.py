from django.contrib import admin
from .models import product, Company
from import_export.admin import ImportExportModelAdmin
from simple_history import register
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.


@admin.register(product)
class productAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'company', 'price', 'category']
    list_display_links = ['name']
    list_filter = ['company__name', 'category']
    search_fields = ['name', 'company__name', 'category']
    ordering = ['id']

    class Meta:
        model = product
        fields = ['id', 'name', 'model', 'company__name', 'category', 'price']


@admin.register(Company)
class companyAdmin(ImportExportModelAdmin, SimpleHistoryAdmin, admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    list_display_links = ['name']
    list_filter = ['category']
    search_fields = ['name', 'category']
    ordering = ['id']

    class Meta:
        model = Company
        fields = ['id', 'name', 'category', 'image']
