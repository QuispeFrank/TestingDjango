from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('engines/', views.EngineView.as_view() , name='engines')
]