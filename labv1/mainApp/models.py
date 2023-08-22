from django.db import models


class Sample(models.Model):
    sample_id = models.CharField(max_length=100)
    weight = models.CharField(max_length=100)
    solvent = models.CharField(max_length=100)
    solvent_volume = models.CharField(max_length=100)
    spike_volume = models.CharField(max_length=100)
    notes = models.TextField()
    analysis_dilution = models.CharField(max_length=100)

    def __str__(self):
        return self.sample_id
