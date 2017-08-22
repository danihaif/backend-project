#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import os
import sys
import csv

def ot_sofit(word):
    nun = False
    caph = False
    if word == "ן":
        nun = True
    if word == "ך":
        caph = True
    return nun | caph


def select_query():

    path = r"C:\Users\Daniel\Desktop\done"
    txt = "Full_DB.txt"
    path_to_text = os.path.join(path , txt)
    print path_to_text
    with open(path_to_text , 'w') as f:
        sys.stdout = f
        sql = "select * from yoav.sandbox2 "
        cur = db.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        for row in results:
            if str(row[0]).__contains__("unspecified") | ot_sofit(row[0][0:2]) :
                continue
            # print row[3]
            # print str(row[0]).strip("\n")
            # word = "ממך"
            # word_from_db = str(row[0]).strip("\n")
            # if word_from_db == word:
            #     print "YES"
            print row[0].strip("\n")+ "," + str(row[1]) + "," + str(row[2]) + "," + str(row[4])  +","+ row[3]
    f.close()


def get_data_from_csv():
    path = r"C:\Users\Daniel\Desktop\done"
    txt = "Full_DB.txt"
    word = "ממש"
    path_to_csv = os.path.join(path , txt)
    with open(path_to_csv, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0].strip(" ") == word:
                print row

if __name__ == '__main__':
    # original_std = sys.stdout
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="1234",  # your password
                         db="yoav")
    select_query()
    # sql = "select count(*) from yoav.texts where word = '" +  " ממך " +"';"
    # print sql
    # cur = db.cursor()
    # cur.execute(sql)
    # results = cur.fetchall()
    # for row in results:
    #     print row

    # get_data_from_csv()