from tempfile import *
from random import *
from string import *
from argparse import *

# define main
def main():

    # buld command line argument parser
    parser = build_parser()

    # parse command line arguments
    args = parser.parse_args()

    # if | --help -h | print usage -> exit
    if args.help:
        print args

    # which file for first names
    if args.male:
        which_file = all_males_file
    elif args.female:
        which_file = all_females_file
    else:
        which_file = random_file

    # get user input
    numFirst = raw_input("How many first names : ")
    numLast = raw_input("How many last names? : ")

    # open files
    tempFile = TemporaryFile(mode="w+b")

    lastFile = open('last.txt', 'r+')

    maleFirstFile = open('malefirst.txt', 'r+')
    femaleFirstFile = open('femalefirst.txt', 'r+')

    # generate
    generate(numFirst, numLast, maleFirstFile, femaleFirstFile, lastFile, tempFile, which_file)

    # close name files
    maleFirstFile.close()
    femaleFirstFile.close()
    lastFile.close()

    # rewind temp file
    tempFile.seek(0)

    # open real file
    emailFile = open('emails.txt', 'w+')

    # copy to temp to real file
    for line in tempFile:
        emailFile.write(line.rstrip()+"\n")


    # close temp and real file
    emailFile.close()
    tempFile.close()

# define generate
def generate(numFirst, numLast, maleFirstFile, femaleFirstFile, lastFile, tempFile, which_file):
    files_first = [maleFirstFile, femaleFirstFile]
    for i in range(0, int(numFirst)):
        first = which_file(files_first).readline().split(' ')[0]
        for j in range(0, int(numLast)):
            last = lastFile.readline().split(' ')[0]
            tempFile.write(first + " " + last + "\n")
        lastFile.seek(0)

def random_file(thisList):
    return choice(thisList)

def all_males_file(thisList):
    return thisList[0]

def all_females_file(thisList):
    return thisList[1]

def build_parser():
    parser = ArgumentParser()

    parser.add_argument("-m", "--male", action = "store_true", help="male first names")
    parser.add_argument("-f", "--female", action = "store_true", help = "female first names" )

    return parser

# execute
if __name__ == "__main__":
    main()
