import unicodedata

import workfiles


def only_word_flexion(word,babla):
    '''remove word flexions'''
    '''clean all flexions if a term matching word doesnt exists '''
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
    return cambridge





def is_first_translation_without_frequency(translations):
    return translations[0].find(')') == -1

def only_four_translations(google):
    '''let only the first 4 translations and remove the other ones'''
    translations = google.split(',')
    google = ','.join(translations[:4])
    return google

def remove_same_translations_without_frequency(google):
    '''removing translation without frequency if there is another'''
    new_trs = []
    translations = google.split(',')
    if is_first_translation_without_frequency(translations):
        has_with_frequency=False
        for translation in translations[1:]:
            ini = translation.find(')')
            term_translation = translation[ini+1:].strip().lower()
            if term_translation == translations[0]:
                has_with_frequency=True
        if has_with_frequency:
            new_trs = translations[1:]
        else:
            new_trs = translations
    else:
        new_trs = translations
    google = ','.join(new_trs)
    return google

def remove_same_word(word,google):
    translations = google.split(',')
    new_trs = []
    for translation in translations :
        ini = translation.find(')')
        if translation.strip() == '':
            continue
        if translation[ini+1:][0].isupper() :
            continue
        if translation[ini+1:].strip().lower() == word.lower() :
            continue
        new_trs.append(translation)
    google = ','.join(new_trs)
    return google

def reorganizeTranslations(word,google):
    """remove a term when have both male and female,
    change the main translation to the front of translations,
    sort the translations by frequency,
    remove terms beggining with "o", "a", "os", "as"
    """
    terms = google.split(',')
    others = {}
    i = 0
    if len(terms) > 1 :
        if terms[0][:-1] == terms[1] and terms[0][-1:] == 'a' :
            i = 1
        if len(terms[0]) == len(terms[1]) and terms[1][-1:] == 'o' and terms[0][-1:] == 'a' :
            i = 1
    while i < len(terms):
        if terms[i][3:4].isupper() and word[0:1].isupper() :
            i+=1
            continue
        if terms[i][0:1] == '(' :
            others[terms[i][3:].lower()] = terms[i][:3]
        else :
            if terms[i] not in others:
                others[terms[i].lower()] = '*'
        i += 1
    others = dict(sorted(others.items(), key=lambda item: item[1], reverse=True))
    google = ''
    for term in others:
        if others[term]=='*' :
            others[term] = ''
        google += others[term]+term+','
    google = google.replace(')a ',')').replace(')o ',')').replace(')os ',')').replace(')as ',')')
    return google

def remove_lower_frequency(google):
    '''remove translations with frequency 2 if there are others with frequency 3'''
    '''removing translations with frequency 1, if there are at least 1 translation with another frequency'''
    exclude_all_frequence1 = False
    exclude_all_frequence2 = False
    if google.find('(2)') >= 0 or google.find('(3)') >= 0:
        exclude_all_frequence1 = True
    if google.find('(3)') >= 0:
        exclude_all_frequence2 = True
    translations = google.split(',')
    new_trs = []
    for translation in translations :
        ini = translation.find(')')
        if translation[1:ini] == '1' and exclude_all_frequence1 == True:
            continue
        if translation[1:ini] == '2' and exclude_all_frequence2 == True:
            continue
        new_trs.append(translation)
    google = ','.join(new_trs)
    if google[-1:] != '\n' :
        google = google+'\n'
    return google






def trim_all(items):
    new_items = []
    if isinstance(items, str):
        list_items = items.split(',')
        for item in list_items:
            item = item.strip()
            item = item.replace('\u200b','')
            new_items.append(item)
        return ','.join(new_items)
    elif isinstance(items, list):
        for item in items:
            item = item.strip()
            item = item.replace('\u200b','')
            new_items.append(item)
        return new_items
    else:
        raise Exception("ocorreu um erro, tipo incompativel")

def remove_duplicated_terms(dic):
    terms = dic.split(',')
    terms = list(set(terms))
    dic = ','.join(terms)
    return dic

def remove_duplicated_terms_freq(dic):
    filtered = []
    without_freq = remove_frequency_str(dic)
    uniqs = list(set(without_freq.split(',')))
    terms = dic.split(',')
    for uniq in uniqs:
        for term in terms:
            t = term.find(')')
            if uniq == term[t+1:]:
                filtered.append(term)
                break
    return ','.join(filtered)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore').decode('ascii')
    return only_ascii

def match_flexions(term, other):
    if len(other) <= 7 or len(term) <= 7:
        return False

    if term[:-3] == other[:-3]:
        return True
    if term[:-3] == other[:-2]:
        return True
    if term[:-3] == other[:-1]:
        return True
    if term[:-3] == other:
        return True

    if term[:-2] == other[:-3]:
        return True
    if term[:-2] == other[:-2]:
        return True
    if term[:-2] == other[:-1]:
        return True
    if term[:-2] == other:
        return True

    if term[:-1] == other[:-3]:
        return True
    if term[:-1] == other[:-2]:
        return True
    if term[:-1] == other[:-1]:
        return True
    if term[:-1] == other:
        return True

    return False

def remove_frequency_lst(terms):
    newterms = []
    for term in terms:
        ini = term.find(')')
        newterms.append(term[ini+1:])
    return newterms

def remove_frequency_str(terms):
    newterms = []
    terms = terms.split(',')
    for term in terms:
        ini = term.find(')')
        newterms.append(term[ini+1:])
    return ','.join(newterms)    

def accentuation_only_matching(yandex,google,reverso,cambridge,linguee):
    '''compare words removing accentuations
    change words without accentuation to words using accentuation
    remove all words that dont match with others
    '''
    terms = yandex.split(',')
    g = google.split(',')
    g = remove_frequency_lst(g)
    r = reverso.split(',')
    r = remove_frequency_lst(r)
    c = cambridge.split(',')
    l = linguee.split(',')
    all = []
    all.extend(g)
    all.extend(r)
    all.extend(c)
    all.extend(l)
    all = list(set(all))
    newyandex = []
    for term in terms:
        has = False
        hasflexion = False
        newterm = ''
        flexion = ''
        for other in all:
            another = remove_accents(other)
            term = term.lower()
            another = another.lower()
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

def only_matching(linguee,google,reverso,cambridge_pt,yandex):
    '''
    remove all words that dont match with others
    '''
    reverso = remove_frequency_str(reverso)
    google = remove_frequency_str(google)
    others = [google,reverso,cambridge_pt,yandex]

    terms = linguee.split(',')
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




def exclude_lengthy_translation(free):
    if len(free) > 99:
        return ''
    else:
        return free

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

def only_word_flexion_free(word,free):
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





def remove_less_half_frequency(reverso):
    '''removing term with less than half frequency from another term'''
    translations = reverso.split(',')
    new_trs = []
    anterior_frequency = 2
    frequency = 0
    for translation in translations :
        ini = translation.find(')')
        txt_freq = translation[1:ini]
        if txt_freq != '' :
            frequency = int(txt_freq)
        if frequency < (anterior_frequency/2) :
            continue
        anterior_frequency = frequency
        new_trs.append(translation)
    reverso = ','.join(new_trs)
    return reverso

def remove_same_word(word,reverso):
    '''removing term equal word'''
    translations = reverso.split(',')
    new_trs = []
    for translation in translations :
        if len(translation.strip()) == 0:
            continue
        ini = translation.find(')')
        if ini == -1:
            if translation.strip().lower() == word :
                continue
        if translation[ini+1:][0].isupper() :
            continue
        if translation[ini+1:].strip().lower() == word :
            continue
        new_trs.append(translation)
    reverso = ','.join(new_trs)
    return reverso

def only_four_translations(reverso):
    '''let only the first 4 translations and remove the other ones'''
    translations = reverso.split(',')
    reverso = ','.join(translations[:4])
    return reverso


def clean_lengthy_definitions(definitions):
    titles = ''.join(['<b>. Collins English Dictionary .</b>','<b>. American Heritage .</b>','<b>. Random House Kernerman .</b>'])
    d = definitions.replace('<br>','<BR>')
    d = d.replace('01.','').replace('02.','').replace('03.','').replace('04.','')
    d = d.replace('05.','').replace('06.','').replace('07.','').replace('08.','')
    d = d.replace('09.','').replace('10.','').replace('11.','').replace('12.','')
    d = d.replace('13.','').replace('14.','').replace('15.','').replace('16.','')
    d = d.replace('1.','').replace('2.','').replace('3.','').replace('4.','')
    d = d.replace('5.','').replace('6.','').replace('7.','').replace('8.','')
    d = d.replace('9.','').replace('10.','').replace('11.','').replace('12.','')
    d = d.replace('13.','').replace('14.','').replace('15.','').replace('16.','')
    lst = d.split('<BR>')
    newlst = []
    cnt = 0
    for item in lst:
        cnt+=1
        if titles.find(item) > -1:
            newlst.append('')
            cnt = 0
        elif len(item) < 60:
            item = item.replace('(','<font color="#00aaff"><u>(')
            item = item.replace(')',')</font></u>')
            item = item.replace('Nautical ','<font color="#00aaff"><u>Nautical </font></u>')
            item = item.replace('Sports ','<font color="#00aaff"><u>Sports </font></u>')
            item = item.replace('Games ','<font color="#00aaff"><u>Games </font></u>')
            item = item.replace('Slang ','<font color="#00aaff"><u>Slang </font></u>')
            item = item.replace('Literally ','<font color="#00aaff"><u>Literally </font></u>')
            item = item.replace('Informal ','<font color="#00aaff"><u>Informal </font></u>')
            item = item.replace('Offensive ','<font color="#00aaff"><u>Offensive </font></u>')
            item = item.replace('Baseball ','<font color="#00aaff"><u>Baseball </font></u>')
            item = item.replace('Animals ','<font color="#00aaff"><u>Animals </font></u>')
            newlst.append(f'{cnt:02}. {item}')
        else:
            cnt-=1
    definitions = '<BR>'.join(newlst)
    if definitions[:4] == '<BR>':
        definitions = definitions[4:]
    if definitions[-4:] == '<BR>':
        definitions = definitions[:-4]
    return definitions

def remove_dirt(cambridge):
    cambridge = cambridge.replace(',-a,',',')
    return cambridge
    
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

        babla = terms[1].strip()
        cambridge_def = terms[2]
        free_def = terms[3]
        mac_def = terms[4]
        google = terms[5]
        reverso = terms[6]
        yandex = terms[7]
        linguee = terms[8]
        cambridge_pt = terms[9]
        free_pt = terms[10].strip()


        babla = only_word_flexion(word,babla)

        cambridge_def = organize_definitions_with_br(cambridge_def)


        free_def = clean_lengthy_definitions(free_def)

        mac_def = clean_lengthy_definitions(mac_def)



        google = reorganizeTranslations(word,google)
        google = remove_lower_frequency(google)
        google = trim_all(google)
        google = remove_same_word(word,google)
        google = remove_same_translations_without_frequency(google)
        google = only_four_translations(google)
        google = remove_duplicated_terms_freq(google)


        reverso = trim_all(reverso)
        yandex = trim_all(yandex)
        linguee = trim_all(linguee)
        cambridge_pt = trim_all(cambridge_pt)
        
        cambridge_pt = remove_dirt(cambridge_pt)

        reverso = remove_less_half_frequency(reverso)
        reverso = remove_same_word(word,reverso)
        reverso = only_four_translations(reverso)
        reverso = remove_duplicated_terms_freq(reverso)

        yandex = accentuation_only_matching(yandex,google,reverso,cambridge_pt,linguee)
        linguee = only_matching(linguee,google,reverso,cambridge_pt,yandex)

        yandex = remove_duplicated_terms(yandex)
        linguee = remove_duplicated_terms(linguee)

        free_pt = clean_infos(free_pt)
        free_pt = only_word_flexion_free(word,free_pt)
        free_pt = exclude_lengthy_translation(free_pt)

        line = f'{word}\t{babla}\t{cambridge_def}\t{free_def}\t{mac_def}\t{google}\t{reverso}\t{yandex}\t{linguee}\t{cambridge_pt}\t{free_pt}\t\t\t\t\n'
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