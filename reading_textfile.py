# Reading_textfile

import os, sys

print(f'File: {__file__}')
print(f'Args: {sys.argv}')
sfile = os.path.abspath(sys.argv[0])
print(f'Reading: {sfile}')


# Exist
# sfile = 'inventoy.txt'
if not os.path.exists(sfile):
    print('File not found')
    exit(1)

# Open the file
# FileNotFoundError: wrong file path

sfile = 'reading_textfile.py'
f = open(sfile, 'r')

# Read a line
line = f.readline()
print(line)

# Read numbers of letters
chars = f.read(10)
print(f'Chars: *{chars}*')

# Position
print(f'Position: {f.tell()} of {os.stat(sfile).st_size}')

# Seek -move to a position in the file
# Zero based
f.seek(0)

# Read all lines
print('--------------------------------------')
for l in f.readlines():
    print(l.strip())


# Close the file
# Allows  other applications to work with it
f.close()