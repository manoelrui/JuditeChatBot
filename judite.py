# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import sys
import sqlite3

if len(sys.argv) > 2:
    print('Invalid Parameters')
    exit(0)
elif len(sys.argv) == 1:
    dbName = 'conversation.db'
else:
    dbName = str(sys.argv[1]) + '.db'

chatBot = ChatBot(
        'Judite',
        storage_adapter='chatterbot.storage.SQLStorageAdapter',
        database='./database.sqlite3',
        preprocessors=[
            'chatterbot.preprocessors.clean_whitespace'
        ]
        )

try:
    conn = sqlite3.connect(dbName)
    cursor = conn.cursor()
except(KeyboardInterrupt, EOFError, SystemExit):
    print('Error - Could not connect with database')

try:
    cursor.execute("""
    SELECT main FROM Conversation;
    """        
    )
except(KeyboardInterrupt, EOFError, SystemExit):
    print('Error - Could not get conversation data')


try:
    chatBot.set_trainer(ListTrainer)
    convList = cursor.fetchall()
    chatBot.train([e[0] for e in convList])

    chatBot.set_trainer(ChatterBotCorpusTrainer)
    chatBot.train('./chatterbot-corpus/chatterbot_corpus/data/portuguese/')
except(KeyboardInterrupt, EOFError, SystemExit):
    print('Error - Could not set trainning the dataset')

print ('')
print('Olá meu nome é %s, bem vindo a ZIM !!!' % chatBot.name);
print('')

while True:
        try:
            request = input('YOU: ')
            response = chatBot.get_response(request)
            
            if float(response.confidence > 0.4):
                print('%s: %s' % (chatBot.name.upper(), response))
            else:
                print('%s: Não entendi' % (chatBot.name.upper()));            
            print('')
        
        except(KeyboardInterrupt, EOFError, SystemExit):
            print('Error - Application error :(')
            break

