from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/calc/', consumers.CalculatorConsumer.as_asgi()),
]