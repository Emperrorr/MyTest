import re
textfile='J:/1 категория.txt' #input("Укажите файл для исследования: ")
with open(textfile, encoding='cp1251') as f:
    a=f.read()
    test=a.split('\n\n')
    for items in test:
        questions = items.split('\n')
        c=r'\d\.\s'
        otv=re.findall(r'\d+', questions[-1])
        del (questions[-1])
        j=0
        for q in questions:
#             if len(questions) ==1:
#                 continue
            j=j+1
            if j==1:
                L=len(q)
                for i in range (1,L):
                    if q[i].isalpha():
                        break
                p= q[i:]
                print(p)
                continue
            if re.search(c,q) and q[0] in otv:
                print ('+', (re.split(c,q,maxsplit=1)[1]).strip())
            elif re.search(c,q) and q[0] not in otv:
                print ('-', (re.split(c,q,maxsplit=1)[1]).strip())
            else:
                print (q)
        print ('')