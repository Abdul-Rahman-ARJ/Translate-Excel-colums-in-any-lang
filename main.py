from googletrans import Translator
import googletrans

translator = Translator()

translated_text = translator.translate('hello', dest='de')
print(translated_text.text)
# print(googletrans.LANGUAGES)
# translated_text = translator.translate('안녕하세요.', dest='ja')
# print(translated_text.text)
#
translated_text = translator.translate('veritas lux mea', src='la')
print(translated_text.text)
