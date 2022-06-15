# скачать все файлы поочереди
# проверить каждую строку
# если нашли "text": - режем по " и копируем 4 кусок (всего 5)
# если нашли "title": - режем по " и 4 кусок заменяем на  entity.alexsmobs. + сохраненное с отрезаным .txt
# каждую строку записываем
import os
import time

from googletrans import Translator

translator = Translator()

directory = 'c:/3/tfcbook/patchouli_books/book/'
directoryplus = '/entries/basic_smithing/'
fileout = open('c:/3/tfcbook/original_i_perevod/basic_smithing.txt', "wt", encoding='utf-8')
for f in os.scandir(directory + 'en_us' + directoryplus):
    if f.is_file() and f.path.split('.')[-1].lower() == 'json':
        filein = open(f.path, 'r')
        fileout.write("\"file\" = \"" + f.path + "\"\n")
        i = 1
        name = ""
        fragment = ""
        while True:
            # считываем строку
            line = filein.readline()
            timesleep = 0
            # прерываем цикл, если строка пустая
            if not line:
                break
            print(str(i) + "  " + str(len(line)) + "   ", end='')
            if "\"text\":" in line:
                timesleep = 5
                a = line.split("\"", 5)
                fragment = a[3]
                print('\n' + 'fragment  ' + fragment)
                fileout.write("\"string\" = \"" + str(i) + "\"\n")
                fileout.write("\"orig\" = \"" + fragment + "\"\n")
                # if "\"title\":" in line:
                #     a = line.split("\"", 5)
                #     name = fragment.split(".", 2)
                #     a[3] ='entity.alexsmobs.' + name[0]
                #     print ('name  ' + a[3])
                res = translator.translate(fragment, src='en', dest='ru')
                line = a[0] + "\"" + a[1] + "\"" + a[2] + "\"" + res.text + "\"" + a[4]
                print('line  ' + line)
                fileout.write("\"pere\" = \"" + res.text + "\"\n")

            i += 1
            time.sleep(timesleep)
        # закрываем файл
        filein.close()
        fileout.write("\n")
fileout.close()

# languages = "Python,Java,Perl,PHP,Swift"
# print(languages.split(",",1))
# ['Python', 'Java,Perl,PHP,Swift']
