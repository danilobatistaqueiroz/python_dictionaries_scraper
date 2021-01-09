word_list = '1001-2000'

def remove_same_word(word, terms):
    listterms = terms.split(',')
    try:
        while word in listterms: listterms.remove(word)
        return ','.join(listterms)
    except:
        return ','.join(listterms)

def clean():
    rd = open (f'../../output/{word_list}-yandex.csv', 'r')
    counter = 0
    output = []
    while True:
        counter+=1
        line = rd.readline()
        if not line :
            break
        line = line[:-1]
        fields = line.split('\t')
        word = fields[0]
        pt = fields[2].lower()
        pt = remove_same_word(word,pt)
        fields[2] = pt
        output.append('\t'.join(fields))
    rd.close()
    file = open(f'../out/{word_list}-yandex.out.csv','w')
    file.write('\n'.join(output))
    file.close()



clean()