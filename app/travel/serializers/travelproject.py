from rest_framework import serializers

from ..models import TravelProject, Place

from ..services.aic import fetch_artwork

from .place import PlaceSerializer


class TravelProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelProject
        fields = ["id", "name"]


class TravelProjectDetailSerializer(TravelProjectSerializer):
    places = PlaceSerializer(many=True, required=False)

    class Meta(TravelProjectSerializer.Meta):
        fields = TravelProjectSerializer.Meta.fields + ["description", "start_date", "places"]

    def create(self, validated_data):
        places_data = validated_data.pop("places", [])
        project = TravelProject.objects.create(**validated_data)
        for place_data in places_data:
            artwork = fetch_artwork(place_data["external_id"])
            Place.objects.create(project=project, title=artwork["title"], **place_data)
        return project

    def update(self, instance, validated_data):
        places_data = validated_data.pop("places", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if places_data is not None:
            instance.places.all().delete()
            for place_data in places_data:
                Place.objects.create(project=instance, **place_data)

        return instance