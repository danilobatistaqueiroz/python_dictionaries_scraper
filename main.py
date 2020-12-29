import config

if config.dictionary == 'thesaurus' :
    from dictionaries.thesaurus import thesaurus


if config.dictionary == 'yandex' :
    from dictionaries.yandex import yandex

