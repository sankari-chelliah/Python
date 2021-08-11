class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD before altered()")
        super(Child,self).altered()
        print("CHILD after altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

print("_"*20)

dad.override()
son.override()

print("_"*20)

dad.altered()
son.altered()
