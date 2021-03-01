import workfiles

def remove_same_word():
    print('removing translation equal word')
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
        translations = terms[2].split(',')
        new_trs = []
        for translation in translations :
            if translation.strip() == '':
                continue
            if translation.strip().lower() == word.lower() :
                continue
            new_trs.append(translation.lower())
        translations_result = ','.join(new_trs)
        if translations_result[-1:] != '\n' :
            translations_result = translations_result+'\n'
        new_line = terms[0]+'\t'+terms[1]+'\t'+translations_result
        workfiles.write_tmpfile(cnt,new_line,'a')
    rd.close()

def initialize(dictionary, word_list):
    workfiles.word_list = word_list
    workfiles.dictionary = dictionary

def start():
    workfiles.rem_tmpfiles()
    remove_same_word()
    workfiles.remove_last_comma()
    workfiles.treat_line1001()
    workfiles.rem_tmpfiles_create_outfile()