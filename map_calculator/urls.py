from django.urls import path
from map_calculator.views import Calculate_distance

urlpatterns = [
    path(
        'calculate_distance/',
        Calculate_distance.as_view(),
        name='calculate_distance',
    ),
]
