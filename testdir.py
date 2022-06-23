import os
import pathlib
import time

# pip install googletrans==3.1.0a0
from googletrans import Translator
# import httpcore
from httpcore import ConnectTimeout, ReadTimeout

timesleep = 0
error_num = 0

def translate(adddir, entry):
    global error_num
    # print(addDir, entry)
    filein = open(os.path.join(enpath + adddir + "/" + entry), 'r')
    mypath = os.path.join(newpath + adddir)
    pathlib.Path(mypath).mkdir(parents=True, exist_ok=True)
    fileout = open(os.path.join(mypath + "/" + entry), "wt", encoding='utf-8')
    print("\n" + adddir + "/" + entry + " :")
    #  i = 1
    while True:
        # считываем строку
        line = filein.readline()
        # прерываем цикл, если строка пустая
        if not line:
            break
        # print(str(i) + "  " + str(len(line)) + "   ", end='')
        if "\"text\":" in line or "\"name\":" in line or "\"description\":" in line:

            a = line.split("\"", 5)
            #  strin = a[3].strip()
            #  print("a[3]:\"" + a[3] + "\"")

            #            strres = ""
            if len(a[3].strip()) > 0:
                if a[3] not in data:
                    res = ""
                    while True:
                        try:
                            time.sleep(timesleep)
                            res = translator.translate(a[3], src='en', dest='ru')
                            # print(res)
                            break  # hz
                        except Exception:
                            print("Exception reset\n")
                            error_num += 1
                            # continue

                    # time.sleep(timesleep)
                    # res = translator.translate(a[3], src='en', dest='ru')

                    strres = res.text.replace("$ (", "$(")  # string.replace(oldStr, newStr, count)
                    strres = strres.replace("$( ", "$(")
                    strres = strres.replace(" )", ")")
                    strres = strres.replace("$(вещь)", "$(thing)")
                    strres = strres.replace("$(предмет)", "$(item)")
                    textout.write(a[3] + "\n")  # надо поменять на запись в словарь
                    textout.write(strres + "\n")  # надо поменять на запись в словарь

                    print('\n' + '(en_us) :' + a[3])
                    line = a[0] + "\"" + a[1] + "\"" + a[2] + "\"" + strres + "\"" + a[4]
                    print('(' + lang + ') :' + strres)

                    data[a[3]] = strres
                else:
                    strres = data[a[3]]
            else:
                strres = a[3]

            # print('\n' + '(en_us) :' + a[3])
            # line = a[0] + "\"" + a[1] + "\"" + a[2] + "\"" + strres + "\"" + a[4]
            # print('(' + lang + ') :' + strres)

        fileout.write(line)
        #  i += 1

    # закрываем файл
    filein.close()
    fileout.close()


def translatefolder(rootdir):
    for entry in os.listdir(rootdir):
        fullentry = os.path.join(rootdir, entry)
        # print(fullentry)
        # print(rootDir + "  :  " + entry + "  " + str(os.path.isfile(fullentry)))
        if os.path.isfile(fullentry) and entry.split('.')[-1].lower() == 'json':
            addDir = rootdir.replace(enpath, "")

            translate(addDir, entry)
            # print(addDir, "   ", entry)
        if os.path.isdir(fullentry):
            translatefolder(fullentry)


# def save_dict_to_file(dic):
#     f = open(os.path.join(newpath + "data_translate.txt"), "w", encoding='utf-8')
#     f.write(str(dic))
#     f.close()
#
#
# def load_dict_from_file():
#     f = open('dict.txt', 'r')
#     data = f.read()
#     f.close()
#     return eval(data)


print('=======================================')
translator = Translator()
path = "c:/22/Lexicon-git-my/Lexicon/src/main/resources/data/lexicon/patchouli_books/lexicon/"

enpath = path + "en_us/"
lang = "ru_ru"
newpath = path + lang + "/"
if not os.path.isdir(newpath):
    os.mkdir(newpath)

data = dict()
file = os.path.join(newpath + "translate.txt")
with open(file, mode='a'):
    pass
with open(file, encoding='utf-8') as file:
    try:
        while True:
            key = next(file).rstrip("\n")
            value = next(file).rstrip("\n")
            data[key] = value
    except StopIteration:
        pass  # Достигнут конец файла

#  print(data)

textout = open(os.path.join(newpath + "translate-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"), "wt", encoding='utf-8')
translatefolder(enpath)
textout.close()
#  save_dict_to_file(data)

f = open(os.path.join(newpath + "data_translate-" + time.strftime("%Y%m%d-%H%M%S") + ".txt"), "w", encoding='utf-8')
for key in data:
    f.write(key + "\n")  # надо поменять на запись в словарь
    f.write(data[key] + "\n")
f.close()
print("Error: " + str(error_num))


# if __name__ == '__main__':
#     main()