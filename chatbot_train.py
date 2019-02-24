# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging 

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
        print('PKMKB : Bye')
        break
    if message.strip() != 'bye' or message.strip() != 'Bye'  :
        reply = bot.get_response(message)
        print('PKMKB :',reply)