from django.db import models

class StreamConfig(models.Model):
    stream_id = models.IntegerField()
    region_id = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"Stream {self.stream_id} (Region {self.region_id})"
