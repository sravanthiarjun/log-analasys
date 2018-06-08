#! /usr/bin/env
import psycopg2
conn = psycopg2.connect(dbname="news")
if conn:
    print("collection establishesd sucessfully")
else:

    print("unsucessfully")

cur = conn.cursor()


def popular_articles():
    print("THE POPULAR ARTICLES ARE:")
    cur.execute("select title,views from common_views limit 3")
    result = cur.fetchall()
    for i in result:
        print (str(i)+" -views")


def popular_authors():
    print("THE POPULAR AUTHORS ARE:")
    cur.execute("select name,views from single_views ")
    result = cur.fetchall()
    for i in result:
        print (str(i)+" -views")


def error_percentage():
    print("THE ERROR '%' IS:")
cur.execute("""select to_char(day, 'Mon DD, YYYY') as day, percentage from
            "errors_percent where percentage > 1.0 group by day, percentage
            "order by"percentage desc;""")
    result = cur.fetchall()
    for i in range(len(result)):
        date = result[i][0]
        errors_percent = result[i][1]
        print("%s--%.1f %%" %(date, errors_percent))
popular_articles()
popular_authors()
error_percentage()
cur.close()
conn.close()
