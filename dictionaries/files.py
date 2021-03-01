import time
import requests
import sys
import os
import traceback 

import os

from subprocess import PIPE, Popen
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

def file_cnt_words(output_file):
    cnt = str(cmdline(f'wc -l {output_file}'))[2:]
    return int(cnt.split(' ')[0])


def reverse_replace(text, old, new, occurrences):
    li = text.rsplit(old, occurrences)
    return new.join(li)

def remove_last_occurr(text, what_to_remove):
    return reverse_replace(text, what_to_remove, '', 1)

def write_file(output_file, content):
    file = open(output_file,"a+")
    file.write(content)

def write_log(log_file, content):
    file = open(log_file,"a+")
    file.write(content)

def initialize_file(output_file, start_line):
    if start_line == 0 :
        file = open(output_file,"w")
        file.write('')
        file.close()
