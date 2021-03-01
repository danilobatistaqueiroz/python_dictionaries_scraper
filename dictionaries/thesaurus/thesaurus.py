import time
import requests
import sys
import os
import traceback 

from dictionaries import files
from dictionaries import helpers

word_list = ''
start_line = 0
input_file = ''
output_file = ''
log_file = ''

def get_mp3_file_path(word_mp3_name):
    return f"mp3/{word_list}/{word_list}-thesaurus-{word_mp3_name}.mp3"
def get_mp3_file(word_mp3_name):
    return f"{word_list}-thesaurus-{word_mp3_name}.mp3"

def get_data(word):
    thesaurus_api_url = "https://tuna.thesaurus.com/pageData/"+word
    request_data = requests.get(thesaurus_api_url)
    return request_data.json()

def ipa_mp3(word_mp3_name, data):
    if 'pronunciation' not in data:
        return '\t\t'
    if data['pronunciation'] is None:
        return '\t\t'
    pronunciation = data['pronunciation']
    if 'ipa' not in pronunciation:
        return '\t\t'
    ipa = pronunciation['ipa']
    spell = ''
    if 'spell' in pronunciation:
        spell = pronunciation['spell']
    fields = ''.join([ipa,'\t'])
    fields = ''.join([fields,spell,'\t'])
    fields = ''.join([fields,'[sound:'+ get_mp3_file(word_mp3_name)+']','\t'])    
    if('audio' not in pronunciation):
        return fields
    audio = requests.get(pronunciation['audio']['audio/mpeg'])
    with open(get_mp3_file_path(word_mp3_name), 'wb') as mp3:
        mp3.write(audio.content)
    return fields

def list_synonyms(data, i_definition, full_synonyms):
    i_synonym = 0
    synonyms = data[i_definition]['synonyms']
    synonym100 = ''
    synonym90 = ''
    synonym50 = ''
    while i_synonym < len(synonyms):
        synonym = synonyms[i_synonym]
        if int(synonym['similarity']) == 100:
            synonym100 = ''.join([synonym100,synonym['term'],','])
        elif int(synonym['similarity']) >= 90:
            synonym90 = ''.join([synonym90,synonym['term'],','])
        elif int(synonym['similarity']) >= 50:
            synonym50 = ''.join([synonym50,synonym['term'],','])
        i_synonym = i_synonym+1
    if synonym100 != '':
        full_synonyms = ''.join([full_synonyms,'<b>'+synonym100+'</b>'])
    elif synonym90 != '':
        full_synonyms = ''.join([full_synonyms,'<font color="#ff0000>'+synonym90+'</font>'])
    elif synonym50 != '':
        full_synonyms = ''.join([full_synonyms,'<font color="#cccccc">'+synonym50+'</font>'])
    return full_synonyms

def reverse_replace(text, old, new, occurrences):
    li = text.rsplit(old, occurrences)
    return new.join(li)

def remove_last_occurr(text, what_to_remove):
    return reverse_replace(text, what_to_remove, '', 1)

def get_thesaurus(word, data):
    content = ipa_mp3(word, data)
    data = data['definitionData']
    data = data['definitions']
    definitions_size = len(data)
    i_definition = 0
    full_synonyms = ''
    definitions = ''
    while i_definition < definitions_size:
        definition = data[i_definition]['definition']
        definitions = ''.join([definitions,definition,','])
        full_synonyms = list_synonyms(data, i_definition, full_synonyms)
        i_definition=i_definition+1
    if len(definitions) > 1:
        definitions = definitions[:len(definitions)-1]
    if full_synonyms != '':
        full_synonyms = remove_last_occurr(full_synonyms, ',')
    definitions = ''.join([definitions,'\t'])
    full_synonyms = ''.join([full_synonyms,'\t'])
    content = ''.join([content,definitions,full_synonyms])
    return content

def read_words():
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
            data = get_data(word)
            thesaurus = '\t\t\t\t\t'
            if data['data'] is not None:
                thesaurus = get_thesaurus(word, data['data'])
            print(thesaurus)
            write_file(word+'\t'+thesaurus+'\n')
        file.close()
    except:
        traceback.print_exc()

def write_file(content):
    file = open(output_file,"a+")
    file.write(content)

def write_log(content):
    file = open(log_file,"a+")
    file.write(content)

def initialize_file():
    if start_line == 0 :
        file = open(output_file,"w")
        file.write('')
        file.close()

def do_job():
    if os.path.exists(output_file):
        cntwords = files.file_cnt_words(output_file)
        if cntwords > 1:
            print('Arquivo existente! '+output_file)
            if cntwords > 999:
                return
            global start_line
            start_line = cntwords+1
    print(f'Iniciando arquivo:{output_file}')
    try:
        initialize_file()
        read_words()
    except:
        traceback.print_exc() 