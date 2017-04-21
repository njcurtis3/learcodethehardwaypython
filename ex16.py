from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file. ByeBye!"
target.truncate()

print "Now I'm going to ask you for 3 lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

lines=(line1, line2, line3)
target.write('\n'.join(lines))
target.write('\n')


print "And finally, we close it."
target.close()

print "and then we open it again"
target = open(filename)

print target.read()
