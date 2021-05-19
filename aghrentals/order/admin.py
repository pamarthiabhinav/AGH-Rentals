from django.contrib import admin
from .models import order
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(order)
class orderAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'prod', 'user', 'bookDate', 'status']
    list_display_links = ['id', 'prod', 'user']
    list_filter = ['prod__name', 'user__username', 'status']
    search_fields = ['prod__name', 'user__username', 'status']
    ordering = ['id']

    class Meta:
        model = order
        fields = ['id', 'prod', 'user',
                  'bookDate', 'bookDays', 'status', 'price']
