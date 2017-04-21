# From the module named sys, import the thing named 'argv'
#      into the current name context.
from sys import argv

# unpack into the two named variables, the values contained
#       in the variable named 'argv'
script, filename = argv

# Calls the open() function and assigns an object of class file into txt.
txt = open(filename)

# prints the filename
print "here's your file %r:" % filename

# read the content of the file
print txt.read()

# Asking user to print filename again
print "Type the filename again:"
file_again = raw_input("> ")

# open file for second time
txt_again = open(file_again)

# close file descriptor
print txt_again.read()
