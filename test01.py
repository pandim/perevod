from googletrans import Translator

translator = Translator()
file = open('c:/2/en_us.txt', 'r')
abc = file.read()
res = translator.translate(abc, src='en', dest='ru')
print(res.text)
