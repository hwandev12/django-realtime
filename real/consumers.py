from channels.generic.websocket import AsyncWebsocketConsumer
import json

class JokesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add('jokes', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard('jokes', self.channel_name)

    async def send_jokes(self, event):
        text_message = event['text']

        if isinstance(text_message, dict):
            text_message = json.dumps(text_message)

        await self.send(text_message)