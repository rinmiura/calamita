from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import index, location, LocationFormView


urlpatterns = [
    path('', index, name='index'),
    path('location', location, name='location'),
    path('create', login_required(LocationFormView.as_view()), name='create')
]
