from os import close


fails=open('kaste.txt', 'a', encoding='UTF-8', )
for i in range(10):
    fails.write("pievieno rindu %d\r\n" % (i+1))


#print(fails.read())

fails=close()