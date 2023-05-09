from django.contrib import admin
from users.models import User

# admin.site.register(User)


@admin.register(User)
class PaylessonsAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'id')
