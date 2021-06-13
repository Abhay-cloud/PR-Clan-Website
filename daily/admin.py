from django.contrib import admin
from daily.models import DailyResult

# Register your models here.
# admin.site.register((DailyResult))

@admin.register(DailyResult)


# to inject js 
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)