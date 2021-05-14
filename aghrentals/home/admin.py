from django.contrib import admin
from .models import issue
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(issue)
class supportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'email', 'status']
    list_display_links = ['email']
    list_filter = ['status']
    search_fields = ['id', 'email']
    ordering = ['-status']

    class Meta:
        model = issue
        fields = ['id', 'first_name', 'last_name',
                  'email', 'mobile', 'message', 'status']
