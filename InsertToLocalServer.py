import MySQLdb
import sys
import csv

def create_table():
    cur = db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS test (
             word varchar(255) NOT NULL,
             year int,
             count INT,
             text_title varchar(30),
             author varchar(30),
                PRIMARY KEY(word,year , author))"""
    cur.execute(sql)


if __name__ == '__main__':
    # original_std = sys.stdout
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         port = 3306,
                         passwd="1234",  # your password
                         db="mini")
    # create_table()
    with open("C:\Users\Daniel\Desktop\done\Final_DB - Copy.csv" ) as f:
        reader = csv.reader(f)
        cur = db.cursor()
        for line in reader:

            sql = "INSERT IGNORE INTO test (word, year, count , author , text_title) VALUES" \
                   "('" + line[0] + "'," + str(line[1])  + "," +  line[2] +" ,'" + line[3] + "','" + line[4] + "')"
            print sql
            cur.execute(sql)
            db.commit()







