# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatBot = ChatBot(
        'Judite',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database='./database.sqlite3'        
        )

convIntro = ['oi', 'olá', 'como você está?', 'como vai?', 'tudo bem?', 
        'estou bem', 'estou bem, e você?']

chatBot.set_trainer(ListTrainer)

chatBot.train(convIntro)

while True:
        try:
            quest = input('You: ')
            response = chatBot.get_response(quest)
            print('Bot: ', response)
        
        except(KeyboardInterrupt, EOFError, SystemExit):
            Print('Application error :(')
            break
