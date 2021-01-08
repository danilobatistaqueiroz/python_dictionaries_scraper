import workfiles

workfiles.word_list = '1-1000'

def add_tabs():
    print('adding tabs')
    rd = workfiles.read_lasttmp_or_output()
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
    rd = workfiles.read_lasttmp_or_output()
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

def validate_lasttmp_or_outputfile(ntabs):
    tmp = workfiles.read_lasttmp_or_output()
    rows = 0
    valid = True
    while True:
        line = tmp.readline()
        rows+=1
        if not line :
            break
        if line.count('\t') != ntabs :
            word = line[:line.find('\t')]
            print('tabulacao diferente:'+str(line.count('\t'))+'-'+word)
            valid = False
    tmp.close()
    if rows != 1000:
        print(f'wrong number of lines in file:{rows}')
        valid = False
    return valid

def rem_spell_synonyms():
    print('removing fields spell and synonyms')
    rd = workfiles.read_lasttmp_or_output()
    cnt = workfiles.new_tmpfile()
    while True:
        line = rd.readline()
        if not line :
            break
        fields = line.split('\t')
        newline = fields[0]+'\t'+fields[1]+'\t'+fields[3]+'\t'+fields[4]+'\n'
        workfiles.write_tmpfile(cnt,newline,'a')
    rd.close()

add_tabs()
rem_definitions_duplicate()
valid = validate_lasttmp_or_outputfile(6)
if valid == True:
    rem_spell_synonyms()
workfiles.rem_tmpfiles_create_outfile()