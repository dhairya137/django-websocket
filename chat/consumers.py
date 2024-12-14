from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("WebSocket connected!")  # Debug print
        await self.accept()

    async def disconnect(self, close_code):
        print(f"WebSocket disconnected with code: {close_code}")  # Debug print
        pass

    async def receive(self, text_data):
        print(f"Received message: {text_data}")  # Debug print
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))