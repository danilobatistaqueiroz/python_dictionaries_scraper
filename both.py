from configparser import ConfigParser
parser = ConfigParser()
parser.read('config.ini')[0]

word_list = parser.get('configurations', 'word_list')
start_line = parser.get('configurations', 'start_line')

ini = 1001
end = 2000

from dictionaries.yandex import yandex
from dictionaries.thesaurus import thesaurus

for i in range(1,38):
    word_list = f'{ini}-{end}'

    thesaurus.word_list = word_list
    thesaurus.start_line = int(start_line)
    thesaurus.input_file = f'input/{word_list}.csv'
    thesaurus.output_file = f'output/{word_list}-thesaurus.csv'
    thesaurus.log_file = f'logs/{word_list}-thesaurus.log'
    thesaurus.do_job()

    input_file = f'input/{word_list}.csv'
    output_file = f'output/{word_list}-yandex.csv'
    yandex.do_job(input_file, output_file)

    ini+=1000
    end+=1000