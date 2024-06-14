class Student:
    def __init__(self):
        self.name=" "
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name = name

obj = Student()
obj.setname("Shivam")
print(obj.getname())