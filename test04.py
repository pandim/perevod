import os
import time

from googletrans import Translator

translator = Translator()
# получим объект файла

for f in os.scandir('c:/3/new01/'):
    if f.is_file() and f.path.split('.')[-1].lower() == 'lang':
        # with open(f.path, 'r') as csvfile:
        #    print(csvfile.read())
        filein = open(f.path, 'r')
        fileout = open('c:/3/new01/ru_ru.lang', "wt", encoding='utf-8')
        #
        # filein = open("c:/3/Alexsmobs/en_us/cachalot_whale.txt", "r")
        # fileout = open("c:/3/Alexsmobs/ru_ru/cachalot_whale.txt", "wt", encoding='utf-8')
        i = 1
        while True:
            # считываем строку
            line = filein.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            line = line[:len(line) - 1]
            print(str(i) + "  " + str(len(line)) + "   ", end='')
            if len(line) > 1:
                if "=" in line:
                    lineSplit = line.split("=", 1)
                    if len(lineSplit[1]) > 0:
                        res = translator.translate(lineSplit[1], src='en', dest='ru')
                        line = lineSplit[0] + "=" + res.text
            # else:
            #    line = ''
            # выводим строку
            print(line)
            fileout.write(line + '\n')
            i += 1
            time.sleep(5)
        # закрываем файл
        filein.close()
        fileout.close()

# languages = "Python,Java,Perl,PHP,Swift"
# print(languages.split(",",1))
# ['Python', 'Java,Perl,PHP,Swift']
