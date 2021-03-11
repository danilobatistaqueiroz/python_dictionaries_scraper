import workfiles
'''extract/remove all fields and let only word'''

def workfile():
    rd = workfiles.read_lasttmp_or_lists()
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

        line = f'{word}\t\t\t\t\n'

        workfiles.write_tmpfile(cnt,line,'a')
    rd.close()

def initialize(dictionary, word_list):
    workfiles.word_list = word_list
    workfiles.dictionary = dictionary
    workfiles.lists = 'commonwords/in'
    workfiles.out = 'commonwords/ou'

def start():
    workfiles.rem_tmpfiles()
    workfile()
    workfiles.remove_last_comma()
    workfiles.treat_line1001()
    workfiles.rem_tmpfiles_create_outfile()