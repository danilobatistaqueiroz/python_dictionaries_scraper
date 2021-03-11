import workfiles
'''remove word flexions'''
'''clean all flexions if a term matching word doesnt exists '''

def only_word_flexion(word,babla):
    ini = 0
    end = len(babla)
    txtini = word+'</b></u>'
    exists_word = False
    while True:
        ini = babla.find(txtini,ini+1)
        if ini>-1:
            exists_word = True
        if ini==-1:
            break
        end = babla.find('<',ini+len(txtini))
    if exists_word:
        if end > -1:
            return babla[:end]
        else:
            return babla
    else:
        return ''

def organize_definitions_with_br(cambridge):
    cambridge = cambridge.replace('. 2.','. <BR>2.')
    cambridge = cambridge.replace('. 3.','. <BR>3.')
    cambridge = cambridge.replace('. 4.','. <BR>4.')
    cambridge = cambridge.replace('. 5.','. <BR>5.')
    cambridge = cambridge.replace('. 6.','. <BR>6.')

    
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
        babla = terms[7].strip()
        babla = only_word_flexion(word,babla)
        line = f'{word}\t{babla}\n'
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