import os

dics = ['cambridge','howjsay']

def rename_move_mp3(word, word_list):
    path = r'../../mp3'
    files = os.listdir( path )
    for dic in dics:
        file = f'{dic}-{word}.mp3'
        if files.count(file) > 0:
            os.system(f'mv ../../mp3/{file} ../../mp3/{word_list}/{dic}/{word_list}-{file}')

def search_mp3(word_list):
    fread = open (f'../../input/{word_list}.csv', 'r')
    counter = 0
    while True:
        counter+=1
        word = fread.readline()
        word = word[:-1]
        if not word :
            break
        rename_move_mp3(word, word_list)
    fread.close()

def create_dirs(word_list):
    for dic in dics:
        os.system(f'mkdir -p ../../mp3/{word_list}/{dic}')

#for i in range(1,14):
    #ini = (i*1000)+1
    #end = (i*1000)+1000
    #word_list = str(ini)+'-'+str(end)
    #create_dirs(word_list)
word_list = '9001-10000'
search_mp3(word_list)