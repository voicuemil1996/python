#Ex.3
from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


#Ex.6
numberSequence = '3, 5, 7, 8'
numberList = numberSequence.split(',')
numberTuple = tuple(numberList)

print(numberList)
print(numberTuple)


#Ex.9
exam_st_date = (11, 12, 2014)
print("%i/ %i/ %i"%exam_st_date)


#Ex. 10
n = 5
print(n + n * 10 + n + n * 100 + n * 10 + n)


#Ex. 13
print("""a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example""")


#Ex. 14 (nr. of days between 2 dates)
from datetime import date

f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date

print(delta.days)


#Ex. 19
def creatingNewString(string):

    if(string.startswith('Is')):

        return string

    else:

        return 'Is' + string

print(creatingNewString('Isomorphic'))
print(creatingNewString('somorphic'))


#Ex. 20
def creatingNewString(string, n):

    newString = string

    for i in range(n - 1):
        newString += string

    return  newString

n = int(input('n = '))
string = input('string = ')

print(creatingNewString(string, n))


#Ex. 41(check if a file exists)
from os import path
print(path.exists("randomfile.txt"))


#Ex. 42
import struct
print(struct.calcsize("P") * 8)


#Ex.49(list all files in a dir)
import os
from os import listdir
from os.path import isfile, join

mypath = os.getcwd()
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)


#Ex. 55
import socket
print(socket.gethostbyname(socket.gethostname()))


#Ex. 57(get execution time)
import time

def randomMethod():

    start_time = time.time()
    print("Nothing important")
    end_time = time.time()

    return  end_time - start_time

print(randomMethod())


#Ex. 70
import glob
import os

files = glob.glob("*")
print(files, '\n')

files.sort(key=os.path.getmtime)
print("\n".join(files))


#Ex. 79(getting syze of an obj in bytes)
import sys

object = [1, "doi", "III"]
print(sys.getsizeof(object))


#Ex.86(ASCII value of a character)
c = 'a'
print(f"ASCII value of {c} is ", ord(c))