from django.urls import path
from . import views

urlpatterns = [
    path("",views.index),
    path("posts",views.posts),
    path("posts/<slug>",views.psots_with_slug)
]