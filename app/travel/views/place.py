from django.db import IntegrityError

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from ..models import Place, TravelProject
from ..serializers.place import PlaceSerializer
from ..services.aic import fetch_artwork


@extend_schema(
    parameters=[
        OpenApiParameter("project_pk", OpenApiTypes.INT, OpenApiParameter.PATH),
    ]
)
class PlaceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PlaceSerializer

    def get_queryset(self):
        return Place.objects.filter(project_id=self.kwargs["project_pk"])

    def create(self, request, *args, **kwargs):
        project = TravelProject.objects.get(pk=self.kwargs["project_pk"])

        if project.places.count() >= 10:
            raise ValidationError("Project cannot have more than 10 places.")

        external_id = request.data.get("external_id")
        artwork = fetch_artwork(external_id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save(project=project, title=artwork["title"])
        except IntegrityError:
            raise ValidationError("This place already exists in the project.")

        return Response(serializer.data, status=status.HTTP_201_CREATED)