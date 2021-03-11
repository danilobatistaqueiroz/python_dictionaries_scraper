import sys
from commonwords import onlywords, clean_babla, equalize_yandex_linguee, clean_freedic, clean_export, clean_all

word_list = 'most_common_04001_05000'
clean_export.clear(word_list)

if sys.argv[1]=='onlywords':
    onlywords.initialize('all',word_list) #exports word \t macmillan-phrases \t freedic-phrases \t macmillan-phrases-pt \t freedic-phrases-pt
    onlywords.start()
elif sys.argv[1]=='cleanbabla':
    clean_babla.initialize('all',word_list) #exports word \t babla-definition
    clean_babla.start()
elif sys.argv[1]=='equalize':
    equalize_yandex_linguee.initialize('all',word_list) #exports word \t yandex-pt \t linguee-definition
    equalize_yandex_linguee.start()
elif sys.argv[1]=='cleanfree':
    clean_freedic.initialize('all',word_list) #exports word \t free-pt
    clean_freedic.start()
elif sys.argv[1]=='all':
    clean_all.initialize('all',word_list)
    clean_all.start()