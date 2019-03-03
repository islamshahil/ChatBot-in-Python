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
    logic_adapter= 
    [
        'chatterbot.logic.BestMatch',
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
    try:
        message = input('You : ')
    except KeyboardInterrupt:
        print ('Alfie : Invalid Input... Aborting!!')
        break
    W_s=message.find('weather')
    W_c=message.find('Weather')
        
    if message.strip() == 'Bye' or message.strip() == 'bye' :
        print('Alfie : Sayonara :-)')
        break
    if message.strip() != 'bye' or message.strip() != 'Bye'  :
        reply = bot.get_response(message)
        if reply.confidence>0.25:
            print('Alfie : ',reply)
        elif reply.confidence<=0.25 :
            print("Alfie : Sorry! I couldn't understand you!!!")

    if message.strip() == 'weather' or message.strip() == 'Weather' or W_s!=-1 or W_c!=-1 :
        try:
            city = input('City Name : ')
        except KeyboardInterrupt:
            print('Invalid Input... Aborting!!')
            break
        api_address='http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
        url = api_address + city
        json_data = requests.get(url).json()
        try:
            format_add = json_data['main']
            print('Alfie : ',format_add)
        except KeyError:
            print("Alfie : Please Enter a City which actually exists!!!")