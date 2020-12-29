def remove_same_word(word, terms):
    return terms.remove(word)



def clean():
    rd = open ('../../../output/3001-4000-yandex.csv', 'r')
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
        pt = pt.replace(',',', ')
        pt = remove_same_word(word,pt)
        fields[2] = pt
        output.append('\t'.join(fields))
    rd.close()
    file = open('../../../output/clean/3001-4000-yandex-clean.csv','w')
    file.write('\n'.join(output))

clean()