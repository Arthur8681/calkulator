import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CalculatorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        try:
            num1 = float(data.get('num1', 0))
            num2 = float(data.get('num2', 0))
            operation = data.get('operation')

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = "Ошибка: деление на ноль" if num2 == 0 else num1 / num2
            else:
                result = "Неверная операция"
        except (ValueError, TypeError):
            result = "Ошибка: введите корректные числа"

        await self.send(text_data=json.dumps({'result': result}))