import workfiles
'''remove word flexions'''
'''clean all flexions if a term matching word doesnt exists '''

def clean_infos(free):
    infos = ['feminine','sometimes','noun','adverb','verb','adjective','etc','plural','<b>eg</b>','especially',
    'past tense past participle','preposition','usually','slang','also','ˈ','ˌ',
    'past tense, past participle']
    for info in infos:
        free = free.replace(info,'')
    free = free.replace('<b></b>','')
    free = free.replace('<b> </b>','')
    return free

def getroot(word):
    if len(word) > 4:
        return word[:3]
    else:
        return word

def remove_number_word(word,free):
    free = free.replace(f'<b>{word}1</b>',f'<b>{word}</b>')
    free = free.replace(f'<b>{word}2</b>',f'<b>{word}</b>')
    free = free.replace(f'<b>{word}3</b>',f'<b>{word}</b>')
    free = free.replace(f'<b>{word}4</b>',f'<b>{word}</b>')
    return free

def only_word_flexion(word,free):
    startword = getroot(word)
    ini = -1
    end = len(free)
    txtini = '<b>'+word+'</b> '
    free=remove_number_word(word,free)
    initial = -1
    while True:
        ini = free.find(txtini,ini+1)
        if ini==-1:
            break
        initial = ini
        end = free.find("<b>"+startword,initial+len(txtini))
        if end == -1:
            end = free.find("<u>"+startword,initial+len(txtini))
            if end == -1:
                end = len(free)
    if initial > -1:
        return free[initial:end]
    else:
        return ''
    
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
        free = terms[15].strip()
        free = clean_infos(free)
        free = only_word_flexion(word,free)
        if len(free) > 99:
            free = ''
        line = f'{word}\t{free}\n'
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