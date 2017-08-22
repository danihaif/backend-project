#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import MySQLdb
from BeautifulSoup import BeautifulSoup
import os

def strip_nikud(word):
    soup = BeautifulSoup(word)
    new_word = ""
    word = soup.contents[0]
    # print word
    for c in word:
        uni = ord(c)
        if uni < 1515 and uni > 1487:
            new_word += c
    if isinstance(new_word, unicode):
        return new_word.encode('utf-8')

def create_table():
    cur = db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS main (
             word varchar(255) NOT NULL,
             year int,
             count INT,
              PRIMARY KEY(word,year))"""
    cur.execute(sql)


def getWords(path):

    with open(path) as tsv:
        wordArray=list()
        for line in csv.reader(tsv, dialect="excel-tab"): #we can also use delimiter="\t" rather than giving a dialect
            try:
                word = line[0].split()
                clean_word = strip_nikud(word[2])
                if len(clean_word) > 1 :
                    wordArray.append(clean_word)
            except:
                pass

        return wordArray

            # for word in line:
            #     print(word)


def insert_to_main(word , year):
    cur = db.cursor()
    sql = "INSERT INTO main (word, year, count) VALUES('" +word + "'," + str(year) +", 1) ON DUPLICATE KEY UPDATE " \
                                                                                   "count=count+1"
    cur.execute(sql)
    db.commit()


def get_new_title(title):
    title_list = str(title).split(".")
    new_title = title_list.__getitem__(0) + "_new." + title_list.__getitem__(1)
    return new_title


def get_new_path(path):
    path_splitted = str(path).split("\\")
    path_len = path_splitted.__len__()
    print str(path_len)
    title = path_splitted.__getitem__(path_len-1)
    print title
    new_path = ""
    for word in path_splitted:
        if word.endswith(".txt"):
            new_path = new_path + get_new_title(word)
        else:
            new_path = new_path + word + os.sep
    return new_path

def move_clean_words_to_output_file(path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            filepath = subdir + os.sep + file
            if filepath.endswith(".txt"):
                new_path = get_new_path(filepath)
                open(new_path , 'w')
                words = list(getWords(filepath))




if __name__ == '__main__':

    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="1234",  # your password
                         db="root")

    #
    # create_table()
    # file = open("C:\Users\yoav\Desktop\out.txt", 'w')
    # import sys
    #
    # sys.stdout = file

    array = getWords(r'C:\cs\tagger.ner\output\adam_hacohen\meixal_dimah.txt')
    # for word in array:
    #     print word
    #     insert_to_main(word,1900)

    # cur = db.cursor()
    # sql = '''select * from main;'''
    # cur.execute(sql)
    # for row in cur.fetchall():
    #     print str(row[0]) +","+ str(row[1]) +","+ str(row[2])