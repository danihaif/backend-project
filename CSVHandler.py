#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
import unicodedata
Path_to_csv = r"C:\Users\yoav\Downloads\Ben_Yehuda - Sheet1.tsv"

def get_author_year_from_csv(author):
    with open(Path_to_csv, 'r') as f:
        reader = csv.reader(f , dialect="excel-tab")
        i = 0
        for row in reader:
            if i == 0:
                i += 1
                pass
            if(row[0] != author):
                pass
            else:
                value = int(row[2]) + int(row[3])
                return value/2

def get_hebrew_author(author):
    with open(Path_to_csv, 'rU') as f:
        reader = csv.reader(f, dialect=csv.excel_tab)
        for row in reader:
            if row[0] != author:
                pass
            else:
                print row[1]
import sys
get_hebrew_author("feierberg")

#
#         # for cell in row:
#         #    rowBuilder = rowBuilder + str(cell) + ","
#         # print rowBuilder[:-1]
