# write text file with functions

import os

#Simplfy mode usage
def toFile(filename, mode, data):
    f = open(filename, mode)
    for i in range(5):
        f.write(str(i) + ':' + data + '\r\n')
    f.close() #Some people use f.flush() but close do the flush job

# Write will overwrite the entire file. You have to be carefull with this. Use append to add to a file!!!!
def writeFile(filename):
    toFile(filename, 'w', 'Hello World')

# Append will add to the end of the file
def appendFile(filename):
    toFile(filename, 'a', 'Hello again!')


# Read the file
def readFile(filename):
    if not os.path.exists(filename):
        print('File not found')
        return
    f = open(filename, 'r')
    # for line in f.readlines():
    #     print(line)
    print(f.read()) #Becarful with this, this read the entire file if too long will take for ever
    f.close()

# See it in action
myfile = 'hello.txt'
writeFile(myfile)
appendFile(myfile)
readFile(myfile)
