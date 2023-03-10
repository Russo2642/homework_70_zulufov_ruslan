from django.contrib import admin
from tracker.models import Issue
from tracker.models import Status
from tracker.models import Type


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'get_types', 'status', 'created_at')
    list_filter = ('id', 'summary', 'description', 'status', 'created_at')
    search_fields = ('summary', 'status')
    readonly_fields = ('id', 'created_at', 'updated_at')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    list_filter = ('id', 'title', 'description', 'created_at')
    search_fields = ('title', )
    readonly_fields = ('id', 'created_at', 'updated_at')


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


admin.site.register(Issue, IssueAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Type, TypeAdmin)
