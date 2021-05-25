from django.db import models
import uuid


class UuidGenerator(models.Model):
    uuid = models.UUIDField(unique=True, default=uuid.uuid4) 
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uuid}"