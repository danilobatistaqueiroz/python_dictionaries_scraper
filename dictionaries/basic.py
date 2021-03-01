html_headers = {
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

def color_word(word,txt):
    txt = txt.replace(word,f'<font color="#ff0000">{word}</font>')
    txt = txt.replace(word.capitalize(),f'<font color="#ff0000">{word.capitalize()}</font>')
    return txt

def blur_color_text(txt):
    return f'<font color="#c7c7c7"><i>{txt}</i></font>'

def emphasie_text(txt):
    return f'<i><u><font color="#aa4444">{txt}</font></u></i>'

def capitalize_first(txt):
    """capitalize the first letter"""
    if txt is not None and len(txt)>1:
        return txt[0:1].upper()+txt[1:]
    else:
        return txt

def insert_end_dot(text):
    text = text.strip()
    if text[-1:] != '.':
        text = text.strip()+'.'
    return text

def insert_quotations(text):
    text = text.strip()
    if text.startswith('"') or text.startswith("'") or text.startswith("´") or text.startswith("`"):
        return text
    else:
        return '"'+text+'"'
