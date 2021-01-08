import os
import shutil
import traceback 

def rename_mp3_to_word(word_list):
    rd = open (f'../../output/{word_list}-thesaurus.csv', 'r')
    counter = 0
    while True:
        counter+=1
        line = rd.readline()
        if not line :
            break
        line = line[:-1]
        fields = line.split('\t')
        start = len(f'[sound:thesaurus-')
        if len(fields) > 6:
            word_mp3 = fields[8][start:-5]
        if len(fields) <= 6:
            continue
        try:
            if os.path.isfile(f'../../mp3/thesaurus-{word_mp3}.mp3'):
                shutil.move(f'../../mp3/thesaurus-{word_mp3}.mp3',f'../../mp3/{word_list}/thesaurus-{word_mp3}.mp3')
        except:
            print(f'error moving {word_list} {word_mp3}')
    rd.close()

for i in range(5,6):
    ini = (i*1000)+1
    end = (i*1000)+1000
    word_list = str(ini)+'-'+str(end)
    if os.path.isfile(f'../../output/{word_list}-thesaurus.csv'):
        rename_mp3_to_word(word_list)