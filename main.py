import config

word_list = config.word_list
start_line = config.start_line

if config.dictionary == 'macmillan' :
    from dictionaries.macmillan import macmillan
    macmillan.word_list = word_list
    macmillan.input_file = f'input/{word_list}.csv'
    macmillan.output_file = f'output/{word_list}-macmillan.csv'
    macmillan.log_file = f'logs/{word_list}-macmillan.log'
    macmillan.do_job()

if config.dictionary == 'thesaurus' :
    from dictionaries.thesaurus import thesaurus
    thesaurus.word_list = word_list
    thesaurus.start_line = int(start_line)
    thesaurus.input_file = f'input/{word_list}.csv'
    thesaurus.output_file = f'output/{word_list}-thesaurus.csv'
    thesaurus.log_file = f'logs/{word_list}-thesaurus.log'
    thesaurus.do_job()

if config.dictionary == 'yandex' :
    from dictionaries.yandex import yandex
    input_file = f'input/{word_list}.csv'
    output_file = f'output/{word_list}-yandex.csv'
    yandex.do_job(input_file, output_file)