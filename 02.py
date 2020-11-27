
txt1 = input("请输入要打开的文件: ")
hamletTxt = open(txt1, "r",encoding='UTF-8').read()
hamletTxt = hamletTxt.lower()
zifu=len(hamletTxt)
juzi=0
danci=0
for ch in hamletTxt:
    if (ch==' '):
        zifu=zifu-1
for ch in hamletTxt:
    if (ch=='.'):
        juzi=juzi+1
words= hamletTxt.split()
danci=len(words)

print("总共有{}个句子".format(juzi))
print("总共有{}个字符".format(zifu))
print("总共有{}个单词".format(danci))

input('Press <Enter>')

