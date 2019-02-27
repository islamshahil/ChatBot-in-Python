# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging 
import requests

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

print("Please be Gramatically correct in your conversation. U'll get prepared for your english exam :-)")

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
    W_s=message.find('weather')
    W_c=message.find('Weather')
        
    if message.strip() == 'Bye' or message.strip() == 'bye' :
        print('Bot : Sayonara :-)')
        break
    if message.strip() != 'bye' or message.strip() != 'Bye'  :
        reply = bot.get_response(message)
        print('Bot : ',reply)

    if message.strip() == 'weather' or message.strip() == 'Weather' or W_s!=-1 or W_c!=-1 :
        city = input('City Name : ')
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + city
        json_data = requests.get(url).json()
        format_add = json_data['main']
        print('Bot : ',format_add)