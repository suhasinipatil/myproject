from django.urls import path
from .views import get_data

urlpatterns = [
    path('api/data.json/', get_data, name='get_data'),
]
