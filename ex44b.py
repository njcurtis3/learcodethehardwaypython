#practice 'Implicit' and 'Override'

# Implcit

class Parent(object):

    def implicit(self):
        print "this is the implicit example"

class Child(Parent):
    pass

example1 = Parent()
example2 = Child()

example1.implicit()
example2.implicit()


# override

class Parent(object):

    def override(self):
        print "this is Parent the override example"

class Child(Parent):

    def override(self):
        print "this is the Child override example"

example1 = Parent()
example2 = Child()

example1.override()
example2.override()

# 3rd example "Before or After"

class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered

# All three combined
# creating Parent class
class Parent(object):
    # override Parent which is self
    def override(self):
        # prints parent message
        print "PARENT override()"
    # define function in parent but not the child
    def implicit(self):
        # print parent message
        print "PARENT implicit()"
    # define function in altered state in the parent
    def altered(self):
        # prints parent message
        print "PARENT altered()"
#create Child class of Parent
class Child(Parent):
    # define override funtion parent.override
    def override(self):
        # prints child message
        print "CHILD override()"
    # define altered function parent.altered
    def altered(self):
        # prints altered child message
        print "CHILD BEFORE PARENT altered()"
        # call super with arguments Child and self then call function altered on ().
        super(Child, self).altered()
        # prints child message after the parent
        print "CHILD AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
