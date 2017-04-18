from tempfile import *
from random import *
from string import *
from argparse import *


# # # # # # # # # # # # # # # # # # #
#                                   #
#       Function Definitions        #
#                                   #
# # # # # # # # # # # # # # # # # # #

# define main
def main():

    # buld command line argument parser
    parser = build_parser()
    # parse command line arguments
    args = parser.parse_args()

    # conditions based on arguments
    if args.text:
        exportFileName = 'testusersinfo.txt'
        delimiter = ' '
    else:
        exportFileName = 'testusersinfo.csv'
        delimiter = ','
    ## which file for first names
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

    # list of first name files
    listOpenFiles = [maleFirstFile, femaleFirstFile]

    # generate
    generate(numFirst, numLast, listOpenFiles, lastFile, tempFile, which_file , delimiter)

    # close name files
    for openFile in listOpenFiles:
        openFile.close()
    lastFile.close()

    # rewind temp file
    tempFile.seek(0)

    # open real export file
    exportFile = open(exportFileName, 'w+')

    # copy to temp to real file
    for line in tempFile:
        exportFile.write(line.rstrip()+"\n")


    # close temp and real file
    exportFile.close()
    tempFile.close()

# define generate
def generate(numFirst, numLast, listOpenFiles, lastFile, tempFile, which_file, delimiter):
    for i in range(0, int(numFirst)):
        first = which_file(listOpenFiles).readline().split(' ')[0]
        for j in range(0, int(numLast)):
            last = lastFile.readline().split(' ')[0]
            tempFile.write(first + delimiter + last + "\n")
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
    parser.add_argument("-f", "--female", action = "store_true", help = "female first names")

    parser.add_argument("-t", "--text", action = "store_true", help = "text file")

    return parser

# # # # # # # # # # # # # # # # # # #
#                                   #
#               Run                 #
#                                   #
# # # # # # # # # # # # # # # # # # #

# execute
if __name__ == "__main__":
    main()
