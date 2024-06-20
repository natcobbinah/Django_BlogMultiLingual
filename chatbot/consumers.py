import json
from channels.generic.websocket import AsyncWebsocketConsumer


class Chatconsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # accept connection
        await self.accept()

    async def disconnect(self, close_code):
        pass

    # receive message from websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # send message to websocket
        await self.send(text_data=json.dumps({'message': message}))
