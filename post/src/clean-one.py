import yandex
import babla

ini = 31001
end = 32000
dic = 'babla'

print(f'limpando {dic} em {ini}-{end}')
word_list = str(ini)+'-'+str(end)
babla.initialize(dic,word_list)
babla.start()