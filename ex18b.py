# this one is like your scripts with argv
def print_three(*args):
    arg1, arg2, arg3 = args
    print "ONE: %r, TWO: %r, THREE: %r" % (arg1, arg2, arg3)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "NADA'."


print_three("Nathan","Shaw","JOEL")
print_two_again("ZedD","Curtis")
print_one("123456789")
print_none()
