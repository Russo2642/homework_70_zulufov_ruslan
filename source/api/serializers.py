from rest_framework import serializers

from tracker.models import Issue

from tracker.models import Project


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = ('id', 'summary', 'description', 'status', 'types', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')


class ProjectSerializer(serializers.ModelSerializer):
    issue = IssueSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id', 'start_date', 'end_date', 'title', 'description', 'created_at', 'updated_at', 'issue')
        read_only_fields = ('id', 'created_at', 'updated_at')
