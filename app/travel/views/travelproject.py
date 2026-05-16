from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from ..models import TravelProject
from ..serializers.travelproject import TravelProjectSerializer, TravelProjectDetailSerializer


class TravelProjectViewSet(viewsets.ModelViewSet):
    queryset = TravelProject.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TravelProjectSerializer
        return TravelProjectDetailSerializer

    def destroy(self, request, *args, **kwargs):
        project = self.get_object()
        if project.places.filter(visited=True).exists():
            raise ValidationError("Cannot delete a project that has visited places.")
        return super().destroy(request, *args, **kwargs)