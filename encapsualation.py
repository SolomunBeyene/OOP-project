class Transport: 

# adding an underscore encapuslates the attributes of the function keeping it hidden
    def __init__(self):
        self._make = "Porsche"
        
    
    def get_make(self): 
        return self._make

    def set_make(self, value_to_set):
        self._make = value_to_set      

vehical = Transport()
print(vehical.get_make())
vehical.set_make("Change Vehical")
print(vehical.get_make())




