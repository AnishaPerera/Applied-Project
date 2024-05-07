from django.contrib import admin
from .models import SearchLog, AdvancedSearchLog

# Register your models here.

class SearchLogAdmin(admin.ModelAdmin):
    readonly_fields=['user','brand','firmware_version']

class AdvancedSearchLogAdmin(admin.ModelAdmin):
    readonly_fields=['user','brand','firmware_version','cve_id','userquery']

admin.site.register(SearchLog, SearchLogAdmin)
admin.site.register(AdvancedSearchLog,AdvancedSearchLogAdmin)