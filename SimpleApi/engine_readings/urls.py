from django.urls import path
from . import views
from .views import FileUploadView

app_name = 'app'
urlpatterns = [
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('engines/', views.EngineView.as_view() , name='engines')
]