from rest_framework import serializers

from ..models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ["id", "external_id", "title", "notes", "visited"]
        read_only_fields = ["id", "title"]

    def update(self, instance, validated_data):
        instance.notes = validated_data.get("notes", instance.notes)
        instance.visited = validated_data.get("visited", instance.visited)
        instance.save()
        return instance