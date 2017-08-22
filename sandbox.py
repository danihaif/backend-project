#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 1488 1514
import unidecode
import os
import csv
from BeautifulSoup import BeautifulSoup
import sys


def get_new_title(title):
    title_list = str(title).split(".")
    new_title = title_list.__getitem__(0) + "_tmp." + title_list.__getitem__(1)
    return new_title


def get_temp_path(path):
    path_splitted = str(path).split("\\")
    path_len = path_splitted.__len__()
    title = path_splitted.__getitem__(path_len - 1)
    print title
    new_path = ""
    for word in path_splitted:
        if word.endswith(".txt"):
            new_path = new_path + get_new_title(word)
        else:
            new_path = new_path + word + os.sep
    return new_path


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


def getWords(path):
    with open(path) as tsv:
        wordList = list()
        for line in csv.reader(tsv, dialect="excel-tab"):  # we can also use delimiter="\t" rather than giving a dialect
            try:
                word = line[0].split()
                clean_word = strip_nikud(word[2])
                if len(clean_word) > 1:
                    wordList.append(clean_word)
            except:
                pass
        return wordList


def move_clean_words_to_output_file(path):
    for subdir, dirs, files in os.walk(path):
        # visited = False
        for file in files:
            # visited = True
            filepath = subdir + os.sep + file
            # iterate only txt files
            if filepath.endswith(".txt") : # and visited:
                # get temporary path to file
                new_path = get_temp_path(filepath)
                # open the file for writing
                fo = open(new_path, 'w')
                # get all words in file
                word_list = getWords(filepath)
                for word in word_list:
                    fo.write(word)
                    fo.write("\n")
                fo.close()
                # remove the original file
                os.remove(filepath)
                # rename tmp file to original file
                os.rename(new_path, filepath)


path = r"C:\Users\yoav\Desktop\ben_yehuda\output"
move_clean_words_to_output_file(path)
