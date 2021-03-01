import time
import requests
import sys
import os
import traceback

from dictionaries.helpers import red

from dictionaries import files
from dictionaries.babla import scraper

word_list = ''
input_file = ''
output_file = ''
log_file = ''

def read_words(start_line):
    print('lendo as linhas do arquivo')
    try:
        file = open(input_file,"r")
        count_line = 0
        for line in file:
            count_line+=1
            if start_line > 0 and count_line < start_line:
                print(count_line)
                continue
            tab_position = line.find('\t')
            word = line[:tab_position]
            print(word)
            if word[0:1].capitalize() == word[0:1]:
                print(red('capitalized (babla)'))
                files.write_file(output_file, word+'\t \n')
                continue
            if word.find("'") > -1:
                print(red('crase (babla)'))
                files.write_file(output_file, word+'\t \n')
                continue
            if len(word) <= 2:
                print(red('menor ou igual a 2 (babla)'))
                files.write_file(output_file, word+'\t \n')
                continue
            time.sleep(1)
            result = scraper.search(word, 'pt', 'ingles', 'portugues')
            print(result[0])
            files.write_file(output_file, word+'\t'+result[0]+'\n')
        file.close()
    except:
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
    if start_line > 0:
        cnt = files.file_cnt_words(output_file)
        if (cnt+1) != start_line:
            print(f'Numero de linhas no arquivo diferente do informado para iniciar: {cnt} e {start_line}')
            return 
    try:
        files.initialize_file(output_file, start_line)
        read_words(start_line)
        print('finalizando o processo do arquivo:'+output_file)
    except:
        print('erro no processamento do arquivo:'+output_file)
        traceback.print_exc() 