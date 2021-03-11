def clear(word_list):
    rd = open(f'commonwords/in/{word_list}-all.csv', 'r')
    txt = rd.read()
    txt = txt.replace('|','')
    rd.close()
    rd = open(f'commonwords/in/{word_list}-all.csv', 'w')
    rd.write(txt)
    rd.close()