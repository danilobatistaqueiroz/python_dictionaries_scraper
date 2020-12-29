from googletrans import Translator
translator = Translator()
translation = translator.translate('expensive', dest='en')
print(translation.text)