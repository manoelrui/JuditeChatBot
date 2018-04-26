# -*- coding: utf-8 -*-
import sqlite3

conn = sqlite3.connect('conversation.db')
cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE Conversation (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        main TEXT NOT NULL
    );
    """);
except sqlite3.OperationalError:
    print('The database already exists')

while True:
    sentence = str(raw_input('Input: '))

    if sentence == '':
        exit(0)

    try:
        cursor.execute("""
        INSERT INTO Conversation (main) VALUES (?)
        """, (str(sentence), )
        )

        conn.commit()
    except sqlite3.OperationalError:
        print('Could not insert sentence %s' % (sentence))
        exit(1)

conn.close()
