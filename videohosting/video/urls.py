from django.urls import path
from .views import VideoListView, VideoCreateView, VideoEmbedDetailView, VideoUploadDetailView


app_name = 'video'

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
    path('create/', VideoCreateView.as_view(), name='video_create'),
    path('detail-upload/<pk>/', VideoUploadDetailView.as_view(), name='video_detail_upload'),
    path('detail-embed/<pk>/', VideoEmbedDetailView.as_view(), name='video_detail_embed'),
]