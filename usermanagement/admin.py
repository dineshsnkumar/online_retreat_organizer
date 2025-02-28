from django.contrib import admin
from .models import Retreat, Teacher, Recording

class RecordingInLine(admin.TabularInline):
    model = Recording


class RetreatInLine(admin.ModelAdmin):
    inlines = [
        RecordingInLine,
    ]

# Register your models here.    
admin.site.register(Retreat, RetreatInLine)
admin.site.register(Teacher)
