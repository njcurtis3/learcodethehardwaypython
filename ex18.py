# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2, = args
    print "arg1: %r, arg2: %r" % (Nathan, Curtis)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2, %r" % (Nathan, Curtis)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % WAHHHHHHHHH

# this one takes no arguments
def print_none():
    print "No arg here'."


print_two("Nathan","Curtis")
print_two_again("Nathan","Curtis")
print_one("WAHHHHHHHHH")
print_none()
