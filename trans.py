from googletrans import Translator
import pandas as pd

translator = Translator()
data = pd.read_excel('test.xlsx')
# 'de': 'german'
# 'fr': 'french'
# 'it': 'italian'
# 'zh-cn': 'chinese (simplified)'

def traslate_german(x):
    return translator.translate(x, dest='de').text

def traslate_french(x):
    return translator.translate(x, dest='fr').text

def traslate_italian(x):
    return translator.translate(x, dest='it').text

def traslate_chinise_simplified(x):
    return translator.translate(x, dest='zh-cn').text


# print(data['en'])
res_ger = list(map(traslate_german, data['en'].head()))
res_french = list(map(traslate_french, data['en'].head()))
res_italian = list(map(traslate_italian, data['en'].head()))
res_ch = list(map(traslate_chinise_simplified, data['en'].head()))
# print(res)
res = {
    0:res_ger,
    1:res_french,
    2:res_italian,
    3:res_ch
}
# print(res)
res1 = pd.DataFrame(res)
print(res1)
res1.to_excel("output.xlsx")
