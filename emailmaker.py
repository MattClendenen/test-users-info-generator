import tempfile
import random
import string

numFirst = raw_input("How many first names : ")
numLast = raw_input("How many last names? : ")

temp = tempfile.TemporaryFile(mode="w+b")

lastFile = open('last.txt', 'r+')

maleFirstFile = open('malefirst.txt', 'r+')
femaleFirstFile = open('femalefirst.txt', 'r+')


files_first = [maleFirstFile, femaleFirstFile]



for i in range(0, int(numFirst)):
    first = random.choice(files_first).readline().split(' ')[0]
    for j in range(0, int(numLast)):
        last = lastFile.readline().split(' ')[0]
        temp.write(first + " " + last + "\n")
    lastFile.seek(0)

maleFirstFile.close()
femaleFirstFile.close()
lastFile.close()

temp.seek(0)

emailFile = open('emails.txt', 'w+')

for line in temp:
    emailFile.write(line.rstrip()+"\n")


emailFile.close()
temp.close()
