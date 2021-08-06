from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User


class UserAdmin(UserAdmin):
	list_display = ('email', 'username', 'timestamp', 'last_login', 'is_admin', 'is_staff')
	search_fields = ('email', 'username')
	readonly_fields = ('timestamp', 'last_login')

	ordering = ('email' , 'username')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(User, UserAdmin)