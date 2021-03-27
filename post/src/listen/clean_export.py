def clear(word_list):
    rd = open(word_list, 'r')
    txt = rd.read()
    txt = txt.replace('|','')
    rd.close()
    rd = open(word_list, 'w')
    rd.write(txt)
    rd.close()