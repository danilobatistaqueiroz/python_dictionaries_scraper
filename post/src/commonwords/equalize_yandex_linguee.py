import workfiles
import unicodedata

def remove_duplicated_terms(dic):
    terms = dic.split(',')
    terms = list(set(terms))
    dic = ','.join(terms)
    return dic

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('ascii')
    return only_ascii

def match_flexions(term, other):
    if term[:-3] == other[:-3]:
        return other
    if term[:-3] == other[:-2]:
        return other
    if term[:-3] == other[:-1]:
        return other
    if term[:-3] == other:
        return other

    if term[:-2] == other[:-3]:
        return other
    if term[:-2] == other[:-2]:
        return other
    if term[:-2] == other[:-1]:
        return other
    if term[:-2] == other:
        return other

    if term[:-1] == other[:-3]:
        return other
    if term[:-1] == other[:-2]:
        return other
    if term[:-1] == other[:-1]:
        return other
    if term[:-1] == other:
        return other

def remove_frequency(terms):
    newterms = []
    for term in terms:
        ini = term.find(')')
        newterms.append(term[ini+1:])
    return newterms

def accentuation_only_matching(yandex,google,reverso,cambridge,linguee):
    '''compare words removing accentuations
    change words without accentuation to words using accentuation
    remove all words that dont match with others
    '''
    terms = yandex.split(',')
    g = google.split(',')
    g = remove_frequency(g)
    r = reverso.split(',')
    r = remove_frequency(r)
    c = cambridge.split(',')
    l = linguee.split(',')
    all = []
    all.extend(g)
    all.extend(r)
    all.extend(c)
    all.extend(l)
    if yandex.find('esguicho') > -1:
        print('moto')
    newyandex = []
    for term in terms:
        has = False
        hasflexion = False
        newterm = ''
        flexion = ''
        for other in all:
            another = remove_accents(other)
            term = term.lower().strip()
            another = another.lower().strip()
            if term == another:
                has = True
                newterm = other
                break
            if match_flexions(term,another):
                hasflexion = True
                flexion = other
        if has:
            newyandex.append(newterm.lower())
        else:
            if hasflexion:
                newyandex.append(flexion.lower())
    return ','.join(newyandex)

def only_matching(dic,others):
    '''
    remove all words that dont match with others
    '''
    terms = dic.split(',')
    matching = []
    all = []
    for other in others:
        items = other.split(',')
        all.extend(items)
    for term in terms:
        has = False
        newterm = ''
        for other in all:
            if term.lower().strip() == other.lower().strip():
                has = True
                newterm = other
                break
        if has:
            matching.append(newterm.lower())
    return ','.join(matching)

def workfile():
    print('working in file')
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

        google = str(terms[2])
        reverso = str(terms[3])
        yandex = str(terms[4])
        cambridge = str(terms[5])
        linguee = str(terms[6])

        yandex = accentuation_only_matching(yandex,google,reverso,cambridge,linguee)
        linguee = only_matching(linguee,[google,reverso,cambridge,yandex])

        yandex = remove_duplicated_terms(yandex)
        linguee = remove_duplicated_terms(linguee)

        line = f'{word}\t{yandex}\t{linguee}\n'

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