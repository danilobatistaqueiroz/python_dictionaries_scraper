import time
import requests
import sys
import os
import traceback

from dictionaries.helpers import red

from dictionaries import files
from dictionaries.macmillan import scraper

word_list = ''
input_file = ''
output_file = ''
log_file = ''

def read_words(start_line):
    try:
        file = open(input_file,"r")
        count_line = 0
        for line in file:
            count_line+=1
            if start_line > 0 and count_line < start_line:
                continue
            tab_position = line.find('\t')
            word = line[:tab_position]
            print(word)
            if word[0:1].capitalize() == word[0:1]:
                print(red('capitalized (macmillan)'))
                files.write_file(output_file, word+'\t\t\t\n')
                continue
            if word.find("'") > -1:
                print(red('crase (macmillan)'))
                files.write_file(output_file, word+'\t\t\t\n')
                continue
            if len(word) <= 2:
                print(red('menor ou igual a 2 (macmillan)'))
                files.write_file(output_file, word+'\t\t\t\n')
                continue
            time.sleep(3)
            result = scraper.search(word)
            files.write_file(output_file, word+'\t'+result[0]+'\t'+result[1]+'\t'+result[2]+'\n')
        file.close()
        print('fim do processamento do arquivo:'+output_file)
    except:
        print('erro no processamento do arquivo:'+output_file)
        traceback.print_exc()

def do_job():
    start_line = 0
    if os.path.exists(output_file):
        cntwords = files.file_cnt_words(output_file)
        if cntwords > 1:
            print('Arquivo existente! '+output_file)
            if cntwords > 999:
                return
            start_line = cntwords+1
    if start_line == 0:
        print(f'Iniciando arquivo:{output_file}')
    else:
        print(f'Continunado:{output_file}')

    try:
        files.initialize_file(output_file, start_line)
        read_words(start_line)
        print('finalizando o processo do arquivo:'+output_file)
    except:
        print('erro no processamento do arquivo:'+output_file)
        traceback.print_exc() 