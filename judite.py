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

while True:
        try:
            request = input('You: ')
            response = chatBot.get_response(request)
            print('Bot: ', response)
            print('')
        
        except(KeyboardInterrupt, EOFError, SystemExit):
            Print('Application error :(')
            break
