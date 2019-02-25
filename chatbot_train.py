# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging 
import requests

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

bot = chatbot = ChatBot('Bot',
    logic_adapters=
    [
        "chatterbot.logic.BestMatch" ,
        "chatterbot.logic.MathematicalEvaluation",
        "chatterbot.logic.TimeLogicAdapter",        
    ],
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
)
	
trainer = ListTrainer(bot)

for files in os.listdir('E:/ChatBot-in-Python-master/english/'):
     data = open('E:/ChatBot-in-Python-master/english/' + files , 'r').readlines()
     trainer.train(data)

while True:
    message = input('You : ')
    
        
    if message.strip() == 'Bye' or message.strip() == 'bye' :
        print('Bot : Bye')
        break
    if message.strip() != 'bye' or message.strip() != 'Bye'  :
        reply = bot.get_response(message)
        print('Bot : ',reply)

    if message.strip() == 'weather' or message.strip() == 'Weather' or message.strip() == 'What is the Weather?' or message.strip() == 'Weather today' or message.strip() == "What's the Weather" :
        city = input('City Name : ')
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + city
        json_data = requests.get(url).json()
        format_add = json_data['main']
        print('Bot : ',format_add)
