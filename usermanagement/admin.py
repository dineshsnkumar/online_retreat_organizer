from django.contrib import admin
from .models import Retreat, Teacher, Recording, Resource

class RecordingInLine(admin.TabularInline):
    model = Recording

class ResourceInLine(admin.TabularInline):
    model = Resource


class RetreatInLine(admin.ModelAdmin):
    inlines = [
        RecordingInLine,
        ResourceInLine,
    ]

# Register your models here.    
admin.site.register(Retreat, RetreatInLine)
admin.site.register(Teacher)
