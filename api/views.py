from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *
from .serializers import *


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # permission_classes = [permissions.IsAuthenticated]


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be viewed or edited.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # permission_classes = [permissions.IsAuthenticated]


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TaskStatusViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TaskStatuss to be viewed or edited.
    """

    queryset = TaskStatus.objects.all()
    serializer_class = TaskStatusSerializer
    # permission_classes = [permissions.IsAuthenticated]


class TaskPriorityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TaskPrioritys to be viewed or edited.
    """

    queryset = TaskPriority.objects.all()
    serializer_class = TaskPrioritySerializer
    # permission_classes = [permissions.IsAuthenticated]
