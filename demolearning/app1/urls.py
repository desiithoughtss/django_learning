from django.urls import path
from . import views

urlpatterns = [
    path("comingHere/", views.comingHere, name="comingHere"),
    path("anotherHere/<int:id>", views.anotherHere, name="anotherHere"),
    path("google/", views.redirecting, name="redirecting"),
    path("<int:id>/", views.newRedirect, name="newRedirect")

]
