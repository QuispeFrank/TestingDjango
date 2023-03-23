from django.urls import path
from . import views


app_name="polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/detalles", views.DetailsView.as_view(), name="details"),
    path("<int:pk>/resultados", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/votos", views.vote, name="votes"),
]