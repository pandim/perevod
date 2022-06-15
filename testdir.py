import os
import pathlib
import time

# pip install googletrans==3.1.0a0
from googletrans import Translator


def Translate(addDir, entry):
    # print(addDir, entry)
    filein = open(os.path.join(enpath + addDir + "/" + entry), 'r')
    mypath = os.path.join(newpath + addDir)
    pathlib.Path(mypath).mkdir(parents=True, exist_ok=True)
    fileout = open(os.path.join(mypath + "/" + entry), "wt", encoding='utf-8')
    print("\n" + addDir + "/" + entry + " :")
    i = 1
    while True:
        # считываем строку
        line = filein.readline()
        timesleep = 0
        # прерываем цикл, если строка пустая
        if not line:
            break
        #print(str(i) + "  " + str(len(line)) + "   ", end='')
        if "\"text\":" in line or "\"name\":" in line or "\"description\":" in line:
            timesleep = 2
            a = line.split("\"", 5)
            print('\n' + '(en_us) :' + a[3])
            # if "\"title\":" in line:
            #     a = line.split("\"", 5)
            #     name = fragment.split(".", 2)
            #     a[3] ='entity.alexsmobs.' + name[0]
            #     print ('name  ' + a[3])
            strres = ""
            if len(a[3].strip()) > 0:
            #if len(a[3]) > 0 and a[3] != " ":
                res = translator.translate(a[3], src='en', dest='de')
                #string.replace(oldStr, newStr, count)
                strres = res.text.replace("$ (", "$(")
                strres = strres.replace("$( ", "$(")
                strres = strres.replace(" )", ")")
                #strres = strres.replace("$(вещь)", "$(thing)")
                #strres = strres.replace("$(предмет)", "$(item)")
                textout.write(a[3] + "\n")
                textout.write(strres + "\n")

            line = a[0] + "\"" + a[1] + "\"" + a[2] + "\"" + strres + "\"" + a[4]
            print(lang + ' :' + strres)
        fileout.write(line)
        i += 1
        time.sleep(timesleep)
    # закрываем файл
    filein.close()
    fileout.close()


def traverfolders(rootdir):
    for entry in os.listdir(rootdir):
        fullentry = os.path.join(rootdir, entry)
        # print(fullentry)
        # print(rootDir + "  :  " + entry + "  " + str(os.path.isfile(fullentry)))
        if os.path.isfile(fullentry) and entry.split('.')[-1].lower() == 'json':
            addDir = rootdir.replace(enpath, "")

            Translate(addDir, entry)
            # print(addDir, "   ", entry)
        if os.path.isdir(fullentry):
            traverfolders(fullentry)


print('=======================================')
translator = Translator()
path = "c:/22/Lexicon-git-my/Lexicon/src/main/resources/data/lexicon/patchouli_books/lexicon/"
enpath = path + "en_us/"
lang = "de_de"
newpath = path + lang + "/"
if not os.path.isdir(newpath):
    os.mkdir(newpath)

textout = open(os.path.join(newpath + "translate.txt"), "wt", encoding='utf-8')
traverfolders(enpath)
textout.close()
