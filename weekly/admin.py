from django.contrib import admin
from weekly.models import WeeklyResult
# Register your models here.
# admin.site.register((WeeklyResult))

@admin.register(WeeklyResult)


# to inject js 
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)