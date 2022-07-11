from django.contrib import admin
from hotel1.models import (
    Cliente,
    )
class ClienteAdmin(admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Cliente,ClienteAdmin)


