from django.db import models
from embed_video.fields import EmbedVideoField


class TitlePlural(models.Model):
    class Meta:
        abstract = True
        ordering = ['created']

    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)


class UploadVideo(TitlePlural):
    file = models.FileField(upload_to='videos/')


class EmbedVideo(TitlePlural):
    file_url = EmbedVideoField()