from django.urls import path

from api.views import *

urlpatterns = [
    path("", MainView.as_view())
]