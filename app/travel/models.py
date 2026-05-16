from django.db import models

class TravelProject(models.Model):
    """manage travel project"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name


class Place(models.Model):
    """manage places"""
    project = models.ForeignKey(
        TravelProject,
        on_delete=models.CASCADE,
        related_name="places",
    )
    external_id = models.IntegerField()
    title = models.CharField(max_length=255, blank=True)
    notes = models.TextField(blank=True, null=True)
    visited = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["project", "external_id"],
                name="unique_place_per_project",
            )
        ]

    def __str__(self):
        return self.title

