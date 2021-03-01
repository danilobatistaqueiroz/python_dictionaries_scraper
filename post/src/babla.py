import workfiles

def remove_volume_up():
    print('removing :volume_up and volume_up')
    rd = workfiles.read_lasttmp_or_output()
    cnt = workfiles.new_tmpfile()
    while True:
        line = rd.readline()
        if not line :
            break
        if len(line) < 5 :
            workfiles.write_tmpfile(cnt,line,'a')
            continue
        terms = line.split('\t')
        if len(terms) == 1 :
            workfiles.write_tmpfile(cnt,line,'a')
            continue
        word = terms[0].strip()
        translations = terms[1].replace('\n','')
        translations = translations.replace(':volume_up,','')
        translations = translations.replace('volume_up,','')
        translations = translations.replace(f'{word}:{word}.','')
        translations = translations.replace(f'<u>{word}</u>:{word}.','')
        translations = translations.replace(f'<u><b>{word}</b></u>:{word}.','')
        translations = translations.replace(f'<b>{word}</b>:{word}.','')

        translations = translations.replace(f'{word}:{word},','')
        translations = translations.replace(f'<u>{word}</u>:{word},','')
        translations = translations.replace(f'<u><b>{word}</b></u>:{word},','')
        translations = translations.replace(f'<b>{word}</b>:{word},','')

        translations = translations.replace(f'{word}:{word} ','')
        translations = translations.replace(f'<u>{word}</u>:{word} ','')
        translations = translations.replace(f'<u><b>{word}</b></u>:{word} ','')
        translations = translations.replace(f'<b>{word}</b>:{word} ','')

        if translations.endswith(word):
            translations = translations.replace(f'{word}:{word}','')
            translations = translations.replace(f'<u>{word}</u>:{word}','')
            translations = translations.replace(f'<u><b>{word}</b></u>:{word}','')
            translations = translations.replace(f'<b>{word}</b>:{word}','')

        capitalWord = word.capitalize()
        translations = translations.replace(f'{capitalWord}:{capitalWord}.','')
        translations = translations.replace(f'<u>{capitalWord}</u>:{capitalWord}.','')
        translations = translations.replace(f'<u><b>{capitalWord}</b></u>:{capitalWord}.','')
        translations = translations.replace(f'<b>{capitalWord}</b>:{capitalWord}.','')

        translations = translations.replace(f'{capitalWord}:{capitalWord},','')
        translations = translations.replace(f'<u>{capitalWord}</u>:{capitalWord},','')
        translations = translations.replace(f'<u><b>{capitalWord}</b></u>:{capitalWord},','')
        translations = translations.replace(f'<b>{capitalWord}</b>:{capitalWord},','')

        translations = translations.replace(f'{capitalWord}:{capitalWord} ','')
        translations = translations.replace(f'<u>{capitalWord}</u>:{capitalWord} ','')
        translations = translations.replace(f'<u><b>{capitalWord}</b></u>:{capitalWord} ','')
        translations = translations.replace(f'<b>{capitalWord}</b>:{capitalWord} ','')

        if translations.endswith(capitalWord):
            translations = translations.replace(f'{capitalWord}:{capitalWord}','')
            translations = translations.replace(f'<u>{capitalWord}</u>:{capitalWord}','')
            translations = translations.replace(f'<u><b>{capitalWord}</b></u>:{capitalWord}','')
            translations = translations.replace(f'<b>{capitalWord}</b>:{capitalWord}','')

        lowerWord = word.lower()
        translations = translations.replace(f'{lowerWord}:{lowerWord}.','')
        translations = translations.replace(f'<u>{lowerWord}</u>:{lowerWord}.','')
        translations = translations.replace(f'<u><b>{lowerWord}</b></u>:{lowerWord}.','')
        translations = translations.replace(f'<b>{lowerWord}</b>:{lowerWord}.','')

        translations = translations.replace(f'{lowerWord}:{lowerWord},','')
        translations = translations.replace(f'<u>{lowerWord}</u>:{lowerWord},','')
        translations = translations.replace(f'<u><b>{lowerWord}</b></u>:{lowerWord},','')
        translations = translations.replace(f'<b>{lowerWord}</b>:{lowerWord},','')

        translations = translations.replace(f'{lowerWord}:{lowerWord} ','')
        translations = translations.replace(f'<u>{lowerWord}</u>:{lowerWord} ','')
        translations = translations.replace(f'<u><b>{lowerWord}</b></u>:{lowerWord} ','')
        translations = translations.replace(f'<b>{lowerWord}</b>:{lowerWord} ','')

        if translations.endswith(lowerWord):
            translations = translations.replace(f'{lowerWord}:{lowerWord}','')
            translations = translations.replace(f'<u>{lowerWord}</u>:{lowerWord}','')
            translations = translations.replace(f'<u><b>{lowerWord}</b></u>:{lowerWord}','')
            translations = translations.replace(f'<b>{lowerWord}</b>:{lowerWord}','')

        translations = translations.replace(',,','').replace('..','').replace(', ,','').replace('. .','')
        translations = translations.replace(':,','').replace(':.','').replace(': ,','').replace(': .','')
        translations = translations.replace(';,','').replace(';.','').replace('; ,','').replace('; .','')
        translations = translations.replace('.,','').replace('.,','').replace('. ,','').replace(', .','')
        translations = translations.replace(',:','').replace('.:','').replace(', :','').replace('. :','')
        translations = translations.replace(',;','').replace('.;','').replace(', ;','').replace('. ;','')
        if translations.startswith('. '):
            translations = translations[2:]
        translations = translations
        new_line = terms[0]+'\t'+translations+'\n'
        workfiles.write_tmpfile(cnt,new_line,'a')
    rd.close()

def initialize(dictionary, word_list):
    workfiles.word_list = word_list
    workfiles.dictionary = dictionary

def start():
    workfiles.rem_tmpfiles()
    remove_volume_up()
    workfiles.remove_last_comma()
    workfiles.treat_line1001()
    workfiles.rem_tmpfiles_create_outfile()