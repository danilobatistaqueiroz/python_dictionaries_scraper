import config

word_list = config.word_list
start_line = config.start_line

if config.dictionary == 'babla' :
    from dictionaries.babla import babla
    minus = word_list.find('-')
    ini = word_list[:minus]
    end = word_list[minus+1:]
    print(f'iniciando babla em {ini}-{end}')
    for i in range(1,41):
        word_list = str(ini)+'-'+str(end)
        babla.word_list = word_list
        babla.input_file = f'input/{word_list}.csv'
        babla.output_file = f'output/{word_list}-babla.csv'
        babla.log_file = f'logs/{word_list}-babla.log'
        babla.do_job()
        ini=int(ini)+1000
        end=int(end)+1000
        start_line = 0
        if ini == 41000:
            break
        if end == 41000:
            end = 41284

if config.dictionary == 'macmillan' :
    from dictionaries.macmillan import macmillan
    minus = word_list.find('-')
    ini = word_list[:minus]
    end = word_list[minus+1:]
    print(f'iniciando macmillan em {ini}-{end}')
    for i in range(1,40):
        word_list = str(ini)+'-'+str(end)
        macmillan.word_list = word_list
        macmillan.input_file = f'input/{word_list}.csv'
        macmillan.output_file = f'output/{word_list}-macmillan.csv'
        macmillan.log_file = f'logs/{word_list}-macmillan.log'
        macmillan.do_job()
        ini=int(ini)+1000
        end=int(end)+1000
        start_line = 0
        if ini == 41000:
            break
        if end == 41000:
            end = 41284

if config.dictionary == 'freedic' :
    from dictionaries.freedic import freedic
    minus = word_list.find('-')
    ini = word_list[:minus]
    end = word_list[minus+1:]
    print(f'iniciando freedic em {ini}-{end}')
    for i in range(1,40):
        word_list = str(ini)+'-'+str(end)
        freedic.word_list = word_list
        freedic.input_file = f'input/{word_list}.csv'
        freedic.output_file = f'output/{word_list}-freedic.csv'
        freedic.log_file = f'logs/{word_list}-freedic.log'
        freedic.do_job()
        ini=int(ini)+1000
        end=int(end)+1000
        start_line = 0
        if ini == 41000:
            break
        if end == 41000:
            end = 41284

if config.dictionary == 'thesaurus' :
    from dictionaries.thesaurus import thesaurus
    minus = word_list.find('-')
    ini = word_list[:minus]
    end = word_list[minus+1:]
    print(f'iniciando thesaurus em {ini}-{end}')
    for i in range(1,40):
        word_list = str(ini)+'-'+str(end)
        thesaurus.word_list = word_list
        thesaurus.start_line = int(start_line)
        thesaurus.input_file = f'input/{word_list}.csv'
        thesaurus.output_file = f'output/{word_list}-thesaurus.csv'
        thesaurus.log_file = f'logs/{word_list}-thesaurus.log'
        thesaurus.do_job()
        ini=int(ini)+1000
        end=int(end)+1000
        start_line = 0
        if ini == 41000:
            break
        if end == 41000:
            end = 41284