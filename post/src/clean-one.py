import yandex
import babla
import thesaurus

ini = 1
end = 1000
dic = 'thesaurus'

print(f'limpando {dic} em {ini}-{end}')
word_list = str(ini)+'-'+str(end)

dictionary = eval(dic)
initialize = getattr(dictionary, 'initialize')(dic,word_list)
start = getattr(dictionary, 'start')()