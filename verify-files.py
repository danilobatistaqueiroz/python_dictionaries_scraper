import os

from dictionaries import files
from dictionaries.helpers import red, blue

for dic in ['thesaurus','babla','freedic','macmillan','yandex']:
    ini = 1001
    end = 2000
    print(f'iniciando {dic} - {ini}-{end}')
    for i in range(1,41):
        word_list = str(ini)+'-'+str(end)
        output_file = f'output/{word_list}-{dic}.csv'

        if os.path.exists(output_file):
            cntwords = files.file_cnt_words(output_file)
            if cntwords > 1:
                if cntwords >= 999:
                    print(f'Arquivo completo! {output_file} com {cntwords} linhas')
                else:
                    print(red(f'Arquivo incompleto! {output_file} com {cntwords} linhas'))
            else:
                print(blue(f'arquivo {output_file} vazio!'))
        else:
            print(red(f'faltando o arquivo {output_file}'))

        ini=int(ini)+1000
        end=int(end)+1000
        if ini >= 41001:
            break
        if end == 41000:
            end = 41284