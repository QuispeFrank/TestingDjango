from django.urls import path
from . import views


app_name="my-polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/detalles", views.details, name="details"),
    path("<int:question_id>/resultados", views.results, name="results"),
    path("<int:question_id>/votos", views.vote, name="votes"),
]