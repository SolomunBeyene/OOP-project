class Transport: # created a class
        #a method (below) is a function that goes inside a class


    def __init__(self, make, model, year): # intialisation. The mercedes name is called through the class car into your function name and then printed
        self.make = make #attributes of the class car
        self.model = model
        self.year = year
    
    def start(self, move = "Forward, backwards"):
        print(move)

    def velocity(self, speed = "Direction and speed"):
        print(speed)   

    def tuning(self, update = "In need of an update"):
        print(update)        

#this is known as a object. Instantiation. This will get passed into your function every time you excute. You can create many objects.
car = Transport("Porsche", "Macan", 2022)
print(car.make, car.model, car.year) 
car.start()  

car2 = Transport("Mercedes", "GLE",2019)
print(car2.model, car2.make)
car2.velocity()
