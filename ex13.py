from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

girls = raw_input("How many girls in AMA do you know?")
cows = raw_input("and cows?")

print "There are more girls %r than %r in Amarillo." % (girls, cows)

print "So you live in amarillo?"
x = raw_input()
print "And for how long?"
y = raw_input()
