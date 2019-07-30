#!/usr/bin/python3

import sqlite3

conn = sqlite3.connect('test.db')
print("opened database successfully")

conn.execute('''CREATE TABLE COMPANY
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEST           NOT NULL,
        AGE INT             NOT NULL,
        ADDRESS        CHAR(50),
        SALARY         REAL);''')

print("TABLE CREATED SUCCESSFULLY")
conn.close()
