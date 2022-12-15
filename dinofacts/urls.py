from django.urls import path

from dinofacts.views import show_dino

urlpatterns = [
    path("show_dino/<str:temp_name>/", show_dino),
]