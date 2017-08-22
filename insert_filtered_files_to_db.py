
import csv
import MySQLdb
from bs4 import BeautifulSoup
import os


def create_table():
    cur = db.cursor()
    sql = """CREATE TABLE IF NOT EXISTS sandbox2 (
             word varchar(255) NOT NULL,
             year int,
             count INT,
             author varchar(30),
             text_title varchar(30),
                PRIMARY KEY(word,year , author))"""
    cur.execute(sql)


def insert_word_to_main(word, year, author, title):
    cur = db.cursor()
    sql = "INSERT IGNORE INTO sandbox2 (word, year, count , author , text_title) VALUES('" + word + "'," + str(year) + \
          ", 1 ,'" + str(author) +"','" + str(title) +"')" + "ON DUPLICATE KEY UPDATE count=count+1"
    print sql
    cur.execute(sql)
    db.commit()


def get_author_from_text(path_to_text):
    path = str(path_to_text).split('\\')
    path.pop()
    author = path.pop()
    return author


def get_hebrew_author(author , path_to_csv):
    with open(path_to_csv, 'rU') as f:
        reader = csv.reader(f, dialect=csv.excel_tab)
        for row in reader:
            if row[0] != author:
                pass
            else:
                return str(row[1])


def get_text_title(path_to_text):
    path = str(path_to_text).split('\\')
    title = path.pop()
    return title


def get_author_year_from_csv(author , path_to_csv):
    with open(path_to_csv, 'rU') as f:
        reader = csv.reader(f , dialect="excel-tab")
        i = 0
        for row in reader:
            if i == 0:
                i += 1
                pass
            if row[0] != author :
                pass
            else:
                value = int(row[2]) + int(row[3])
                return value / 2


def strip_commas(word):
    toClean = [',','.','..','...','!','?',":" , ";","'"]
    for ch in toClean:
        word = word.translate(None,ch)
    return word

def insert_all_words_to_db(path_to_txt_dir, path_to_csv):
    i = 0
    for subdir, dirs, files in os.walk(path_to_txt_dir):
        for file in files:
            file_path = subdir + os.sep + file
            # iterate only txt files
            if file_path.endswith(".txt") :
                if i % 2 == 0 :
                    print file_path
                    author = get_author_from_text(file_path)
                    heb_author = get_hebrew_author(author , path_to_csv)
                    heb_author = strip_commas(heb_author)
                    year = get_author_year_from_csv(author , path_to_csv)
                    title = get_text_title(file_path)
                    for word in open(file_path , 'rU'):
                        word_length = len(word)
                        if word_length > 5:
                            insert_word_to_main(word , year , heb_author , title)
                i += 1





if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="1234",  # your password
                         db="yoav")
    create_table()
    texts_path = r"C:\Users\Daniel\Desktop\output"
    tsv_path = r"C:\Users\Daniel\Downloads\Ben_Yehuda - Sheet1.tsv"

    insert_all_words_to_db(texts_path , tsv_path)