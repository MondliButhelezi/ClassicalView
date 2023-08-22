from django.db import models
import uuid


# Create your models here.
class EquipmentType(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    last_update = models.DateTimeField(auto_now=True)
    last_update_by = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    notes = models.TextField(null=True, blank=True, max_length=300)


class MonitoringStation(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    last_update = models.DateTimeField()
    last_update_by = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    equipment_type_uuid = models.ForeignKey(
        EquipmentType, on_delete=models.CASCADE, related_name='monitoring_units'
    )

    def __str__(self):
        return f"{self.name}: Updated by {self.last_update_by}"

    def is_valid(self):
        pass
