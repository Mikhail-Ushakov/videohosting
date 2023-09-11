from django.forms import ModelForm
from .models import UploadVideo, EmbedVideo


class EmbedForm(ModelForm):
    class Meta:
        model = EmbedVideo
        fields = ['title', 'file_url']


class UploadForm(ModelForm):
    class Meta:
        model = UploadVideo
        fields = ['title', 'file']