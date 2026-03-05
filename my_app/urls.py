from django.urls import path
from my_app.views import first

urlpatterns = [
    path("", first, name = "first_view"),
]
  