# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatbot = ChatBot(
        'Judite',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database='./database.sqlite3'
        )

convIntro = ['oi', 'olá', 'como você está?', 'como vai?', 'tudo bem?', 
        'estou bem']

chatBot.set_trainer(ListTrainer)

chatBot.train(convIntro)
chatBot.train()

while True:
        quest = input('You: ')
        response = bot.get_response(quest)
        print('Bot: ', response)
