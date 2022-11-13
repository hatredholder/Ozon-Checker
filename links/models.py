from django.db import models


class Link(models.Model):
    """URL Link Info Model"""

    name = models.CharField(max_length=220, blank=True)
    url = models.URLField()
    current_price = models.FloatField(default=0)
    old_price = models.FloatField(default=0)
    price_difference = models.FloatField(default=0)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ("price_difference", "-created")
