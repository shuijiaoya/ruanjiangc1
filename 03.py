txt1 = input("请输入要打开的文件: ")
hTxt = open(txt1, "r",encoding='UTF-8').readlines()
hangshu=len(hTxt)
damahang=0
konghang=0
zhushihang=0

for i in range(hangshu-1):
    strs=hTxt[i]
    if(strs[0]==' '):
        konghang=konghang+1
    if(strs[0]=='/'):
        zhushihang=zhushihang+1

damahang=hangshu-zhushihang-konghang

    
print("总共有{}行".format(hangshu))
print("总共有{}行代码".format(damahang))
print("总共有{}行注释".format(zhushihang))
print("总共有{}行空行".format(konghang))

input('Press <Enter>')

