class DemoClass:
    a=10
    def showvalue(self):
        self.c = self.a*self.a
        print(self.c)
    
    def showvalue1(self,a,b):
        print(a*b)

obj = DemoClass()
obj.showvalue()
obj.showvalue1(2,3)
