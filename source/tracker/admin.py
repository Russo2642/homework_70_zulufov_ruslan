from django.contrib import admin

from tracker.models import Issue

from tracker.models import Type

from tracker.models import Status


# Register your models here.
class IssueAdmin(admin.ModelAdmin):
    list_display = ('id', 'summary', 'description', 'status', 'type', 'is_deleted', 'created_at')
    list_filter = ('id', 'summary', 'description', 'status', 'type', 'is_deleted', 'created_at')
    search_fields = ('summary', 'status')
    readonly_fields = ('id', 'created_at', 'updated_at')


admin.site.register(Issue, IssueAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


admin.site.register(Type, TypeAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_filter = ('id', 'name')


admin.site.register(Status, StatusAdmin)
