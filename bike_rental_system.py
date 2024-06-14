class BikeShop:
    def __init__(self,stock):
        self.stock = stock
    def displayBike(self):
        print("\nTotal Bike: ", self.stock)
    def rentForBike(self,q):
        if q<=0:
            print("Enter the positive value or greater than zero")
        elif q> self.stock:
            print("Enter Available Quantity")
        else:
            self.stock= self.stock-q
            print("Total Price: ", q*100)
            print("\nTotal Bike Available: ",self.stock)
            
obj = BikeShop(100)
while True:
    user_choice = int(input('''
1) Quantity Display
2) Bike Rent
3) Exit
   Select Choice Number: '''))
    if user_choice==1:
        obj.displayBike()
    elif user_choice==2:
        n = int(input("Enter Buy Qunatity: "))
        obj.rentForBike(n)
    else:
        break
