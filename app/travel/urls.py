from django.urls import path, include
from rest_framework_nested import routers

from .views.travelproject import TravelProjectViewSet
from .views.place import PlaceViewSet

router = routers.DefaultRouter()
router.register("projects", TravelProjectViewSet, basename="project")

projects_router = routers.NestedDefaultRouter(router, "projects", lookup="project")
projects_router.register("places", PlaceViewSet, basename="project-places")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(projects_router.urls)),
]