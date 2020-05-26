import math
from car import Car
class RaceCar(Car):
    sound = "Peep Peep\nBeep Beep"
    def __init__ (self,color,max_speed,acceleration,tyre_friction):
        self._nitro=0
   
        super().__init__(color,max_speed,acceleration,tyre_friction)
       
    @property
    def nitro(self):
        return self._nitro
            
    def accelerate(self):
        if self._is_engine_started == True:
            if(self._nitro >= 10):
                self._nitro = self._nitro-10
                self._current_speed = self._current_speed+self._acceleration+math.ceil(self._acceleration*0.3)
                if self._current_speed>self._max_speed:
                    self._current_speed = self._max_speed
            elif self._current_speed + self._acceleration<=self._max_speed:
                self._current_speed = self._current_speed+self._acceleration
            else:
                self._current_speed = self._max_speed
        else:
            print("Start the engine to accelerate")
                    
    def apply_brakes(self):
        if(self._current_speed>self._max_speed/2):
            self._nitro = self._nitro+10
            self._current_speed = self._current_speed-self._tyre_friction
        else:
            if(self._current_speed-self._tyre_friction >= 0):
                self._current_speed = self._current_speed-self._tyre_friction
            else:
                self._current_speed=0
                    