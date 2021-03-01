import thesaurus
import yandex
import babla

ini = 2001
end = 3000
dic = 'babla'

for i in range(1,41):
    print(f'limpando {dic} em {ini}-{end}')
    word_list = str(ini)+'-'+str(end)
    babla.initialize(dic,word_list)
    babla.start()
    ini=int(ini)+1000
    end=int(end)+1000
    start_line = 0
    if ini == 41001:
        break
    if end == 41000:
        end = 41284
