import requests
import sys
import os
import traceback 

INPUT_FILE_PATH = "thesaurus/input/{word_list_name}/{word_list_name}-mixed.csv"
OUTPUT_FILE_PATH = "thesaurus/output/{word_list_name}/{word_list_name}-thesaurus.csv"
BUFFER_FILE_PATH = "thesaurus/output/{word_list_name}/{word_list_name}-thesaurus.log"
MP3_FILE_PATH = "thesaurus/output/{word_list_name}/mp3/thesaurus-{word_mp3_name}.mp3"

def get_input_file_path(word_list_name):
    return INPUT_FILE_PATH.replace('{word_list_name}',word_list_name)
def get_output_file_path(word_list_name):
    return OUTPUT_FILE_PATH.replace('{word_list_name}',word_list_name)
def get_buffer_file_path(word_list_name):
    return BUFFER_FILE_PATH.replace('{word_list_name}',word_list_name)
def get_mp3_file_path(word_list_name, word_mp3_name):
    return MP3_FILE_PATH.replace('{word_list_name}',word_list_name).replace('{word_mp3_name}',word_mp3_name)

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
    ipa = pronunciation['ipa']
    spell = pronunciation['spell']
    fields = ''.join([ipa,'\t'])
    fields = ''.join([fields,spell,'\t'])
    if('audio' not in pronunciation):
        return fields
    audio = requests.get(pronunciation['audio']['audio/mpeg'])
    with open(get_mp3_file_path(word_list_name, word_mp3_name), 'wb') as mp3:
        mp3.write(audio.content)
    return fields

def list_synonyms(data, i_definition, full_synonyms):
    i_synonym = 0
    synonyms = data[i_definition]['synonyms']
    while i_synonym < len(synonyms):
        synonym = synonyms[i_synonym]
        if int(synonym['similarity']) == 100:
            full_synonyms = ''.join([full_synonyms,'<b>'+synonym['term']+'</b>',','])
        elif int(synonym['similarity']) >= 90:
            full_synonyms = ''.join([full_synonyms,'<u>'+synonym['term']+'</u>',','])
        i_synonym = i_synonym+1
    return full_synonyms

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
        full_synonyms += list_synonyms(data, i_definition, full_synonyms)
        i_definition=i_definition+1
    if len(definitions) > 1:
        definitions = definitions[:len(definitions)-1]
    if full_synonyms != '':
        full_synonyms = full_synonyms[:len(full_synonyms)-1]
    definitions = ''.join([definitions,'\t'])
    full_synonyms = ''.join([full_synonyms,'\t'])
    content = ''.join([content,definitions,full_synonyms])
    return content

def readFile(word_list_name, start_line, end_line):
    file = open(get_input_file_path(word_list_name),"r")
    full_content = ''
    count_line = 0
    for line in file:
        count_line+=1
        if start_line > 0 and count_line < start_line:
            continue
        if end_line > 0 and end_line == count_line:
            break
        tab_position = line.find('\t')
        word = line[:tab_position]
        print(word)
        data = get_data(word)
        input_line = line.replace('\n','')
        full_content = ''.join([full_content, input_line])
        if data['data'] is not None:
            thesaurus = get_thesaurus(word, data['data'])
            full_content = ''.join([full_content,thesaurus])
        full_content += '\n'
    file.close()
    return full_content

def writeFile(content, word_list_name):
    file = open(get_output_file_path(word_list_name),"a+")
    file.write(content)

def writeBuffer(content, word_list_name):
    file = open(get_buffer_file_path(word_list_name),"a+")
    file.write(content)

if len(sys.argv) == 1:
    print('informe o nome da lista de palavras')
word_list_name = str(sys.argv[1])
start_line = 0
if len(sys.argv) == 3:
    start_line = int(sys.argv[2])
end_line = 0
if len(sys.argv) == 4:
    end_line = int(sys.argv[3])
try:
    content = readFile(word_list_name, start_line, end_line)
    writeFile(content, word_list_name)
except:
    traceback.print_exc() 
    writeBuffer(content, word_list_name)