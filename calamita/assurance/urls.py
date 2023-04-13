from django.urls import path

from .views import ChainView, NodesView


urlpatterns = [
    path('chain/', ChainView.as_view()),
    path('nodes/', NodesView.as_view())
]
