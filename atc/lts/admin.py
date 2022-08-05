from django.contrib import admin

from .models import ServiceRequest


# Register your models here.
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'ref', 'title', 'status')


admin.site.register(ServiceRequest, ServiceRequestAdmin)
