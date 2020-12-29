from configparser import ConfigParser
parser = ConfigParser()
parser.read('config.ini')[0]
word_list = parser.get('configurations', 'word_list')
dictionary = parser.get('configurations', 'dictionary')
start_line = parser.get('configurations', 'start_line')