import json
from channels.generic.websocket import AsyncWebsocketConsumer
from . import chat_gpt


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
        chat_gpt_response = chat_gpt.chat_completions(message)
        #print(chat_gpt_response)
        await self.send(text_data=json.dumps({'message': chat_gpt_response}))
