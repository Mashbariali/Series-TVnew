from .models import Series
from django.contrib import admin
from django.contrib import messages



class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating')

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

admin.site.register(Series, SeriesAdmin)




