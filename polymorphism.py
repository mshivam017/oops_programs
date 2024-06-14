class Ws:
    def displayinfo(self):
        print("Welcome to WsTube")

class IIP(Ws):
    def displayinfo(self):
        super().displayinfo() #without super method child class(IIP) is Overwrite from Parent Class(Ws)
        print("Welcome to IIP")

obj = IIP()
obj.displayinfo()