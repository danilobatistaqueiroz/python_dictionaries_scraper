import requests
from bs4 import BeautifulSoup

headers = {
   'Content-Type': 'application/xhtml+xml',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST,OPTIONS',
    'Access-Control-Allow-Headers': '*',
    'Access-Control--Max-Age': '86400',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'

}

languagues = {'english':'ingles','portuguese':'portugues','spanish':'espanol','french':'frances','germani':'alemao'}

def convert_lang(language):
    if language in languagues:
        return languagues[language]
    else:
        return language

def search(word, abrv_target, lang_source, lang_target):
    lang_source = convert_lang(lang_source)
    lang_target = convert_lang(lang_target)
    lst_definitions = []
    with requests.Session() as session:
        source = session.get(f'https://{abrv_target}.bab.la/dicionario/{lang_source}-{lang_target}/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")
        quick_results = soup.find_all('div', class_='quick-result-overview')
        count = 0
        for result in quick_results:
            lst_txt = result.get_text().split('\n')
            lst_txt = [x for x in lst_txt if x]
            if abrv_target.upper() in lst_txt:
                div_term = result.find_previous('div', class_='quick-result-option')
                if div_term is not None:
                    bab_result = div_term.find('a', class_='babQuickResult')
                    term = ''
                    if bab_result is not None:
                        term = bab_result.get_text()
                    count+=1
                    lst_txt.remove(abrv_target.upper())
                    if term == word or term == f'to {word}':
                        term = f'<b>{term}</b>'
                    lst_definitions.append('<u>'+term+'</u>:'+','.join(lst_txt))
    return ['. '.join(lst_definitions)]


#print(search('milk','pt','english','portuguese'))