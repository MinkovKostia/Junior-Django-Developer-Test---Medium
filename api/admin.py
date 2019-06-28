from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username', 'phone_number', 'user__first_name', 'user__last_name')
    list_display = ('user', 'phone_number', 'birth_date')
    list_filter = ('birth_date',)


admin.site.register(Profile, ProfileAdmin)
