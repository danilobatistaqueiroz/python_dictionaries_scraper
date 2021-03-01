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

def color_word(word,txt):
    txt = txt.replace(word,f'<font color="#ff0000">{word}</font>')
    txt = txt.replace(word.capitalize(),f'<font color="#ff0000">{word.capitalize()}</font>')
    return txt

def blur_color_text(txt):
    return f'<font color="#c7c7c7"><i>{txt}</i></font>'

def blur_explanation_bold_phrase(txt):
    dot = txt.find(':')
    if dot > 0:
        explanation = txt[:dot+1]
        phrase = txt[dot+1:]
        explanation = blur_color_text(explanation)
        phrase = f'<b>{phrase}</b>'
        txt = explanation + phrase
    else:
        txt = f'<b>{txt}</b>'
    return txt

def insert_end_dot(text):
    if text is None:
        return ''
    text = text.strip()
    if text[-1:] != '.':
        text = text.strip()+'.'
    return text

def capitalize_first(txt):
    """capitalize the first letter"""
    if txt is not None and len(txt)>1:
        return txt[0:1].upper()+txt[1:]

def search(word):
    txt_definitions = []
    txt_examples = []
    txt_ipas = []
    with requests.Session() as session:
        source = session.get(f'https://www.macmillandictionary.com/us/dictionary/american/{word}', headers=headers).text
        soup = BeautifulSoup(source, "html.parser")
        cntdef=0
        senses = soup.find_all('div', class_='SENSE-CONTENT')
        for sense in senses:
            span_definition = sense.find('span', class_='DEFINITION')
            if span_definition is None:
                continue
            cntdef+=1
            txt_def = span_definition.text.replace('\n',' ').replace('  ',' ')
            txt_def = capitalize_first(txt_def)
            sections = txt_def.split(':')
            if len(sections) > 1:
                sections[1] = capitalize_first(sections[1])
                txt_def = '<u>'+sections[0]+'</u>: '+sections[1]
            else:
                txt_def = sections[0]
            txt_def = insert_end_dot(txt_def)
            txt_definitions.append(f'{cntdef}. {txt_def}')

            span_prons = sense.find_all('span', class_='PRON')
            for pron in span_prons:
                txt_ipa = pron.text.replace('  ',' ').replace('/','')
                txt_ipas.append(txt_ipa)

            div_examples = sense.find_all('div', class_='EXAMPLES')
            if len(div_examples) > 0:
                txt_def = blur_color_text(f'{cntdef}. {txt_def}')
                txt_examples.append(txt_def)
            for p_example in div_examples:
                text = p_example.text.replace('\n',' ').replace('  ',' ')
                text = capitalize_first(text)
                text = insert_end_dot(text)
                text = color_word(word,text)
                text = blur_explanation_bold_phrase(text)
                txt_examples.append(text)

    return ['<br>'.join(txt_definitions), ', '.join(txt_ipas), '<br>'.join(txt_examples)]