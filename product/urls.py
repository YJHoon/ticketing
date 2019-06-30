from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create, name="create"),
    path('movie/', views.movie, name="movie"),
    path('list/', views.list, name="list"),
    path('kind/', views.kind, name="kind"),
]