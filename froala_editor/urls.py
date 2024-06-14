from django.urls import path
from froala_editor import views

urlpatterns = [
    path(r'image_upload/', views.image_upload, name='froala_editor_image_upload'),
    path(r'file_upload/', views.file_upload, name='froala_editor_file_upload'),
]
