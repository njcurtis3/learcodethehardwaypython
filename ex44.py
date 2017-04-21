# define a function in the parent, NOT the child
class Parent(object):

    def implicit(self):
        print "Parent implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# override the function in the child, effectively replacing the functionality.
class Parent(object):

    def override(self):
        print "Parent override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()


#practice 'Implicit' and 'Override'

# Implcit

class Parent(object):

    def implicit(self):
        print "this is the implicit example"

class Child(object):

    pass

example1 = Parent()
example2 = Child()

example1.implicit()
example2.implicit()
