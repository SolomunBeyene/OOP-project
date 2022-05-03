from encapsualation import Transport

class Boat(Transport):

    def __init__(self):
        super().__init__()

    def cap(self, freight = "Hold Cargo"):
        print(freight) 

    def pas(self, passenger = "Take Passenger"): 
        print(passenger)   

yoat = Boat()
print(yoat.make())

    