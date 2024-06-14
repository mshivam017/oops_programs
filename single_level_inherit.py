class A:
    def displayA(self):
        print("Welcome to Class A")

class B(A):
    def displayB(self):
        print("Welcome to Class B")

objB = B()
objB.displayB()
objB.displayA()