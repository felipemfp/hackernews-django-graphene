from django.db import models


class Link(models.Model):
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    posted_by = models.ForeignKey('users.User', null=True, on_delete=models.deletion.CASCADE)
