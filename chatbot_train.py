# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import logging 

logger = logging.getLogger() 
logger.setLevel(logging.CRITICAL)

bot = ChatBot('Bot')
trainer = ListTrainer(bot)
#trainer = bot.set_trainer(ListTraner)

for files in os.listdir('E:/ChatBot-in-Python-master/english/'):
     data = open('E:/ChatBot-in-Python-master/english/' + files , 'r').readlines()
     trainer.train(data)

while True:
    message = input('You:')
    if message.strip() != 'Bye' :
        reply = bot.get_response(message)
        print('ChatBot :',reply)
        
    if message.strip() == 'Bye':
        print('ChatBot : Bye')
        break