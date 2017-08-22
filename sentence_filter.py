#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

# import MySQLdb # for later use


def get_output_path_of_txt_file(original_path):
    split = re.split(r"\\", original_path)
    end = split.pop()
    pre_end = split.pop()
    output_txt = output_dir + "\\" + str(pre_end) + "\\" + str(end)
    return output_txt


def get_output_dir_of_txt_file(original_path):
    split = re.split(r"\\", original_path)
    split.pop()
    pre_end = split.pop()
    output_txt = output_dir + "\\" + str(pre_end)
    return output_txt


def filter_beginning(input_dir , unsuccessful_list):
    for subdir, dirs, files in os.walk(input_dir):
        for filename in files:
            found_sentence = 0
            if filename.endswith(".txt"):
                original_file_path = os.path.join(input_dir, subdir, filename)
                path_to_txt_file = get_output_path_of_txt_file(original_file_path)
                path_to_txt_file_dir = get_output_dir_of_txt_file(original_file_path)
                if os.path.exists(path_to_txt_file_dir) == 0:
                    os.mkdir(path_to_txt_file_dir)
                try:
                    with open(original_file_path) as f:
                        for line in f:
                            if found_sentence == 1:
                                output_file = open(path_to_txt_file, 'w')
                                sys.stdout = output_file
                                for row in f:
                                    print row
                                break
                            if sentence_to_filrer in line:
                                found_sentence = 1
                except Exception as e:
                    unsuccessful_list.append(original_file_path)
                    print str(e)

def remove_letochen(output_dir):
    for subdir, dirs, files in os.walk(output_dir):
        for filename in files:
            file_path = os.path.join(output_dir , subdir , filename)
            print file_path
            tochen_counter = 0
            to_break = False
            with open(file_path , 'r') as f:
                lines = f.readlines()
                f.close()
                g = open(file_path, "w")
                for line in lines:
                    if line != "\n":
                        if line != tochen + "\n" :
                            g.write(line)
                        else:
                            if tochen_counter == 0:
                                tochen_counter += 1
                            else:
                                to_break = True
                        if to_break:
                            break

                g.close()



if __name__ == '__main__':
    output_dir = r"C:\Users\yoav\Desktop\ben_yehuda\outputs"
    orig_stdout = sys.stdout
    unsuccessful_list = []
    sentence_to_filrer = "יומן הרשת של פרויקט בן-יהודה"
    tochen = "לתוכן הענינים"
    tochen2 = "לתוכן" + "\n\n" + "הענינים"


    input_dir = r"C:\Users\yoav\Downloads\benyehuda_sep2016_dump_with_nikkud_utf8"
    filter_beginning(input_dir=input_dir , unsuccessful_list = unsuccessful_list)
    sys.stdout = orig_stdout
    remove_letochen(output_dir)
    sys.stdout.close()
    sys.stdout = orig_stdout
    print unsuccessful_list