# this is the simplified version
from sys import argv
from os.path import exists

scripts, from_file, to_file = argv

print (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

out_file = open(to_file, 'w')
out_file.write(indata)

out_file.close()
in_file.close()
