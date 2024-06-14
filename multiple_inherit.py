class A:
    def displayA(self):
        print("Welcome to Class A")

class B:
    def displayB(self):
        print("Welcome to Class B")

class C(A,B):
    def displayC(self):
        print("Welcome to Class C")

objB = C()
objB.displayC()
objB.displayB()
objB.displayA()