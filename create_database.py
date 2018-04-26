# -*- coding: utf-8 -*-
import sqlite3
import sys

dbName = None
if len(sys.argv) > 2:
    print('Invalid parameters')
    exit(0)
elif len(sys.argv) == 1:
    dbName = 'conversation.db'
else:
    dbName = str(sys.argv[1]) + '.db'

conn = sqlite3.connect(dbName)
cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE Conversation (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        main TEXT NOT NULL
    );
    """);
    print('Created the database %s' % (dbName))
except sqlite3.OperationalError:
    print('The database %s already exists' % (dbName))

while True:
    sentence = str(input('Input: '))

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
