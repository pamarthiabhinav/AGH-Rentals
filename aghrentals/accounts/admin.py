from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserSession, UserProfile
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from django.contrib.sessions.models import Session


# Register your models here.


@admin.register(UserSession)
class UserSessionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'user', 'session']
    list_display_links = ['user']
    list_filter = ['user']
    search_fields = ['user']
    ordering = ['id']

    class Meta:
        model = UserSession
        fields = ['id', 'user', 'session']


@admin.register(UserProfile)
class UserSessionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['id', 'username']
    list_display_links = ['username']
    search_fields = ['username__name']
    ordering = ['id']

    class Meta:
        model = UserSession
        fields = ['id', 'username', 'propic']


@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    # remove other sessions
    Session.objects.filter(usersession__user=user).delete()

    # save current session
    request.session.save()

    # create a link from the user to the current session (for later removal)
    UserSession.objects.get_or_create(
        user=user,
        session=Session.objects.get(pk=request.session.session_key)
    )
