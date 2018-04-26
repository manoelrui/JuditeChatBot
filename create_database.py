# -*- coding: utf-8 -*-
import sqlite3
import sys

databaseName = None
if len(sys.argv) > 2:
    Print('Invalid parameters')
    exit(0)
elif len(sys.argv) == 1:
    databaseName = 'conversation.db'
else:
    databaseName = str(sys.argv[1]) + '.db'

conn = sqlite3.connect(databaseName)
cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE Conversation (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        main TEXT NOT NULL
    );
    """);
    print('Created the database %s' % (databaseName))
except sqlite3.OperationalError:
    print('The database %s already exists' % (databaseName))

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
