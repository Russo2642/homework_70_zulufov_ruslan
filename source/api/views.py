from api.serializers import ProjectSerializer, IssueSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tracker.models import Project, Issue


class ProjectDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        try:
            project = Project.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': str(e)})
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)


class IssueDetailView(APIView):
    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        try:
            issue = Issue.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': str(e)})
        serializer = IssueSerializer(issue)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProjectUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            project = Project.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': str(e)})
        serialize = ProjectSerializer(instance=project, data=request.data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
        return Response(serialize.data)


class IssueUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        try:
            issue = Issue.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': str(e)})
        serialize = IssueSerializer(instance=issue, data=request.data)
        if serialize.is_valid(raise_exception=True):
            serialize.save()
        return Response(serialize.data)


class ProjectDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            project = Project.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': str(e)})
        project.delete()
        return Response({"message": f"Project with id {pk} has been deleted."})


class IssueDeleteView(APIView):
    def delete(self, request, pk, *args, **kwargs):
        try:
            issue = Issue.objects.get(pk=pk)
        except Exception as e:
            return Response({'error': str(e)})
        issue.delete()
        return Response({"message": f"Issue with id {pk} has been deleted."})
