from typing import Any
from django.db import models
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .models import EmbedVideo, UploadVideo
from .forms import EmbedForm, UploadForm

class VideoListView(ListView):
    model = EmbedVideo
    template_name = 'video/video_list.html'
    context_object_name = 'embed_video'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['upload_video'] = UploadVideo.objects.all()
        return context
    

class VideoCreateView(CreateView):
    template_name = 'video/video_create.html'
    success_url = reverse_lazy('video:video_list')
    form_class = EmbedForm
    second_form_class = UploadForm

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class()
        if 'form2' not in context:
            context['form2'] = self.second_form_class()
        return context
    
    def post(self, request, *args, **kwargs):
        if 'form' in request.POST:
            form_class = self.get_form_class()
            form_name = 'form'
        else:
            form_class = self.second_form_class
            form_name = 'form2'

        form = self.get_form(form_class)

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(**{form_name: form})


class VideoUploadDetailView(DetailView):
    model = UploadVideo
    template_name = 'video/video_upload_detail.html'


class VideoEmbedDetailView(DetailView):
    model = EmbedVideo
    template_name = 'video/video_embed_detail.html'
