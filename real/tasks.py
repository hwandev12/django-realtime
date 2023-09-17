from .models import Joke
from .serializers import JokeSerializer
from celery import shared_task
import json

from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

channel_layer = get_channel_layer()

@shared_task
def get_joke():
    joke = Joke.objects.all()
    serializer = JokeSerializer(joke, many=True)
    json_data = json.dumps(serializer.data)
    async_to_sync(channel_layer.group_send)("jokes", {"type": "send_jokes", "text": json_data})