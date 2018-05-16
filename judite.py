# -*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot
import sys
import sqlite3
import time
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText


class GuiChatbot(tk.Tk):
    def __init__(self, db_name='conversation.db', *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.chatbot = ChatBot(
                'Judite',
                storage_adapter='chatterbot.storage.SQLStorageAdapter',
                database='./database.sqlite3',
                preprocessors=[
                    'chatterbot.preprocessors.clean_whitespace'
                    ]
                )

        try:
            conn = sqlite3.connect(db_name)
            cursor = conn.cursor()
        except(KeyboardInterrupt, EOFError, SystemExit):
            print('Error - Could not connect with database')
            exit(0)

        try:
            cursor.execute(
                """
                SELECT main FROM Conversation;
                """
            )
        except(KeyboardInterrupt, EOFError, SystemExit):
            print('Error - Could not get conversation data')
            exit(0)

        try:
            self.chatbot.set_trainer(ListTrainer)
            convList = cursor.fetchall()
            self.chatbot.train([e[0] for e in convList])

            self.chatbot.set_trainer(ChatterBotCorpusTrainer)
            self.chatbot.train('./chatterbot-corpus/chatterbot_corpus/data/portuguese/')
        except(KeyboardInterrupt, EOFError, SystemExit):
            print('Error - Could not set trainning the dataset')

        self.initialize()

    def initialize(self):
        self.grid()

        self.respond = ttk.Button(self, text='Get Response', command=self.get_response)
        self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = ttk.Entry(self, state='normal')
        self.usr_input.grid(column=1, row=0, sticky='nesw', padx=3, pady=3)

        self.conversation_lbl = ttk.Label(self, anchor=tk.E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText.ScrolledText(self, state='disabled')
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)

    def get_response(self):
        request = self.usr_input.get()
        self.usr_input.delete(0, tk.END)

        response = self.chatbot.get_response(request)

        self.conversation['state'] = 'normal'
        self.conversation.insert(
                tk.END, "YOU: " + request + "\n" +
                self.chatbot.name.upper() + ": " +
                str(response.text) + "\n\n"
                )
        self.conversation['state'] = 'disabled'

        time.sleep(0.5)


if len(sys.argv) > 2:
    print('Invalid Parameters')
    exit(0)
elif len(sys.argv) == 1:
    dbName = 'conversation.db'
else:
    dbName = str(sys.argv[1])

gui_chatbot = GuiChatbot(dbName)
gui_chatbot.mainloop()
