import requests
import json
import traceback
import os

def readFile(input_file):
    full_content = ''
    try:
        file = open(input_file,"r")
        count_line = 0
        for line in file:
            count_line+=1
            tab_position = line.find('\t')
            word = ''
            if tab_position > 0 :
                word = line[:tab_position]
            else :
                line_break = line.find('\n')
                word = line[:line_break]
            print(word)
            data = get_data(word)
            ipa = transcriptions(data)
            ipa = ','.join(ipa)
            tra = translations(data)
            tra = ','.join(tra)
            full_content = ''.join([full_content, word, '\t', ipa, '\t', tra])
            full_content += '\n'
        file.close()
        print('finalizando yandex, processamento do arquivo:'+input_file)
    except:
        print('yandex, erro no processamento do arquivo:'+input_file)
        traceback.print_exc() 
    return full_content

def writeFile(output_file, content):
    file = open(output_file,"a+")
    file.write(content)

def get_data(word):
    api_url = f'https://dictionary.yandex.net/dicservice.json/lookupMultiple?ui=en&srv=tr-text&sid=efd3f474.5fde63d1.9aecc523.74722d74657874&text={word}&dict=en.syn%2Cen.ant%2Cen.deriv%2Cen-pt.regular&flags=103'
    request_data = requests.get(api_url)
    return request_data.json()

def remove_dups_list(items):
    return list(set(items))

def transcriptions(data):
    ts = []
    for pt in data["en-pt"]["regular"] :
        if "ts" in pt :
            ts.append(pt["ts"])
    ts = remove_dups_list(ts)
    return ts

def translations(data):
    txt = []
    for pt in data["en-pt"]["regular"] :
        for tr in pt["tr"] :
            txt.append(tr["text"])
            if "syn" in tr :
                for syn in tr["syn"]:
                    txt.append(syn["text"])
    txt = remove_dups_list(txt)
    return txt

def do_job(input_file, output_file):
    if os.path.exists(output_file):
        print('Arquivo existente! '+output_file)
        return
    print(f'Iniciando arquivo:{output_file}')
    full_content = readFile(input_file)
    writeFile(output_file, full_content)
