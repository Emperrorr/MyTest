import os
path_in= input('укажите папку для сортировки:')
path_out= input('укажите папку для вывода:')
ext=('txt')
a=int()
cat=os.walk(path_in, topdown=True, onerror=None, followlinks=False)

for path, folder, files in cat:
    for file in files:
#         print (file, path)
        if os.path.isfile(os.path.join(path, file)):
            if (file.endswith(ext)):
                str1 = path + r"/" + file
                str2 = path + r"/" + file[:file.rfind('.')]
#                 os.system('converter.vbs  "' + str1 + '" "' + str2 + '"')
                a+=1
#                 print (str1)
print (a,' file(s) converted')