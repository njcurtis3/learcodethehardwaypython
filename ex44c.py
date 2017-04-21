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

# using super() with __init__

class other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

    son = Child()

    son.implicit()
    son.override()
    son.altered()
    
