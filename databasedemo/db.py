import sqlite3

dbconnect=sqlite3.connect("demo.db")

dbconnect.execute("""CREATE TABLE IF NOT EXISTS MOVIES
        (ID INT PRIMARY KEY NOT NULL,
         TITLE TEXT NOT NULL,
         YEAR   INT NOT NULL,
         TYPE  TEXT NOT NULL) """)

#dbconnect.execute("INSERT INTO MOVIES (ID, TITLE, YEAR, TYPE) values ( 1, 'Shrek', 2001, 'Movie')")
#dbconnect.execute("INSERT INTO MOVIES (ID, TITLE, YEAR, TYPE) values ( 2, 'Shrek the Third', 2007, 'Movie')")
#dbconnect.execute("INSERT INTO MOVIES (ID, TITLE, YEAR, TYPE) values ( 3, 'Shrek the Musical', 2013, 'Broadway Play')")

#dbconnect.execute("update movies set year = 2008 where id = 2")
#dbconnect.commit()

#dbconnect.execute("delete from movies where type != 'Movie'")
#dbconnect.commit()

cursor=dbconnect.execute("select * from MOVIES")
for x in cursor:
    print(f"The {x[3].lower()} '{x[1]}' came out in {x[2]}!")

dbconnect.close()
