
    #!/usr/bin/env python
import psycopg2

conn = psycopg2.connect(database="news", user="vagrant", password="vagrant")

if conn:
    print("connection established Successfully")

else:
    print("Unable to connect")

cur = conn.cursor()


def articles_view():
    cur.execute("select title,likes  from article_view limit 3;")
    find = cur.fetchall()
    print("The most popular three articles:")
    for i in find:
        print(str(i)+" - views")


def author_view():
    cur.execute("select name,views  from authors_view ;")
    find = cur.fetchall()
    print("The most popular article authors:")
    for i in find:
        print(str(i)+" - views")


def log_error_view():
    cur.execute("select * from log_view where percentage_errors > 1 ;")
    find = cur.fetchall()
    print("On which day did more than 1%  of errors found:")
    for i in find:
        print(str(i)+" - errors")

articles_view()
author_view()
log_error_view()
cur.close()
conn.close()
