import sqlite3
conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute("INSERT  INTO EMPLOYEES VALUES (1,'FAITH KARIMI',23,345000.00)")
conn.execute("INSERT  INTO EMPLOYEES VALUES (2,'BOB MARLEY',23,150000.00)")
conn.execute("INSERT  INTO EMPLOYEES VALUES (3,'JOY MAURA',22,200000.00)")
conn.execute("INSERT  INTO EMPLOYEES VALUES (4,'JACOB ELORDI',33,234000.00)")
conn.execute("INSERT  INTO EMPLOYEES VALUES (5,'SHONDA RHIMES',28,655000.00)")

conn.commit()
print("Records inserted successfully")
conn.close()
