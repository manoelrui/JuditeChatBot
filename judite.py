# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
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
        database='./database.sqlite3'
        )

conn = sqlite3.connect(dbName)
cursor = conn.cursor()

cursor.execute("""
SELECT main FROM Conversation;
"""        
)

chatBot.set_trainer(ListTrainer)

convList = cursor.fetchall()
chatBot.train([e[0] for e in convList])

print('Olá meu nome é %s, bem vindo a ZIM !!!' % chatBot.name);
print('')

while True:
        try:
            request = input('YOU: ')
            response = chatBot.get_response(request)
            
            if float(response.confidence > 0.6):
                print('%s: %s' % (chatBot.name.upper(), response))
            else:
                print('%s: Não entendi' % (chatBot.name.upper()));            
            print('')
        
        except(KeyboardInterrupt, EOFError, SystemExit):
            Print('Application error :(')
            break
