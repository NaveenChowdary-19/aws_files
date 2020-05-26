from oop_assignment_001.car import Car
class Truck(Car):
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        self._max_cargo_weight=max_cargo_weight
        self._load=0
        super().__init__(color,max_speed,acceleration,tyre_friction)
    @property 
    def max_cargo_weight(self):
        return self._max_cargo_weight
        
    def load(self,cargo):
        if cargo<0:
            raise ValueError("Invalid value for cargo_weight")
        if self._current_speed==0:
            if cargo<self._max_cargo_weight and self._is_engine_started==False:
                self._load+=cargo
            else:
                print("Cannot load cargo more than max limit: {}".format(self._max_cargo_weight))
        else:
            print("Cannot load cargo during motion")
            
    def unload(self,cargo1):
        if(self._current_speed>0):
            print("Cannot unload cargo during motion")
        if cargo1<0:
            raise ValueError("Invalid value for cargo_weight")
            
    def sound_horn(self):
        if(self._is_engine_started==True):
            print("Honk Honk")
        else:
            print("Start the engine to sound_horn")
            
        
    