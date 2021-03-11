import yandex
import babla

ini = 8001
end = 9000
dic = 'babla'

print(f'limpando {dic} em {ini}-{end}')
word_list = str(ini)+'-'+str(end)

dictionary = eval(dic)
initialize = getattr(dictionary, 'initialize')(dic,word_list)
start = getattr(dictionary, 'start')()