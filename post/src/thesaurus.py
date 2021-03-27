import workfiles

def add_tabs():
    print('adding tabs')
    rd = workfiles.read_lasttmp_or_lists()
    cnt = workfiles.new_tmpfile()
    while True:
        line = rd.readline()
        if not line :
            break
        if line.count('\t') == 1 :
            line = line[:-1] + '\t\t\t\t\t\n'
        if line.count('\t') == 5 :
            first_tab = line.find('\t')
            line = line[:first_tab] + '\t' + line[first_tab:]
        workfiles.write_tmpfile(cnt,line,'a')
    rd.close()

def rem_definitions_duplicate():
    rd = workfiles.read_lasttmp_or_lists()
    cnt = workfiles.new_tmpfile()
    while True:
        line = rd.readline()
        if not line :
            break
        fourth_tab = line.find('\t')
        fourth_tab = line.find('\t',fourth_tab+1)
        fourth_tab = line.find('\t',fourth_tab+1)
        fourth_tab = line.find('\t',fourth_tab+1)
        fifth_tab = line.find('\t',fourth_tab+1)
        definitions = line[fourth_tab+1:fifth_tab]
        list_definitions = definitions.split(',')
        list_uniq = list(dict.fromkeys(list_definitions))
        str_definitions = ','.join(list_uniq)
        line = line[:fourth_tab+1] + str_definitions + line[fifth_tab:]
        workfiles.write_tmpfile(cnt,line,'a')
    rd.close()

def rem_spell_synonyms():
    print('removing fields spell and synonyms')
    rd = workfiles.read_lasttmp_or_lists()
    cnt = workfiles.new_tmpfile()
    while True:
        line = rd.readline()
        if not line :
            break
        line = line.replace('\n','')
        fields = line.split('\t')
        newline = fields[0]+'\t'+fields[1]+'\t'+fields[3]+'\t'+fields[4]+'\n'
        workfiles.write_tmpfile(cnt,newline,'a')
    rd.close()

def sound_mp3_directory():
    print('change the reference of sound in mp3 field')
    rd = workfiles.read_lasttmp_or_lists()
    cnt = workfiles.new_tmpfile()
    while True:
        line = rd.readline()
        if not line :
            break
        line = line.replace('\n','')
        fields = line.split('\t')
        fields[2] = workfiles.add_wordlist_dictionary_soundmp3(fields[2])
        newline = fields[0]+'\t'+fields[1]+'\t'+fields[2]+'\t'+fields[3]+'\n'
        workfiles.write_tmpfile(cnt,newline,'a')
    rd.close()

def initialize(dictionary, word_list):
    workfiles.word_list = word_list
    workfiles.dictionary = dictionary

def start():
    workfiles.rem_tmpfiles()
    add_tabs()
    rem_definitions_duplicate()
    valid = workfiles.validate_number_tabs(6)
    if valid == True:
        rem_spell_synonyms()
        sound_mp3_directory()
        workfiles.treat_line1001()
        workfiles.rem_tmpfiles_create_outfile()