'''class Deer:
       
    sound = "Buck Buck"
    breath = "Breathe in air"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        if age_in_months >= 2:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
            
        self._age_in_months = age_in_months
        
        if required_food_in_kgs <= 0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
            
        self._required_food_in_kgs = required_food_in_kgs
        self._breed = breed
        
        
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 2
    
    def make_sound(self):
        print(self.sound)
    
    def breathe(self):
        print(self.breath)
        
class Lion(Deer):
    
    sound = "Roar Roar"
    breath = "Breathe in air"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 4
        
class Shark(Deer):
    
    sound = "Shark Sound"
    breath = "Breathe oxygen from water"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 8
        
class GoldFish(Deer):
    
    sound = "Hum Hum"
    breath = "Breathe oxygen from water"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.2

class Snake(Deer):
    
    sound = "Hiss Hiss"
    breath = "Breathe in air"
    
    def __init__(self, age_in_months = 0, breed = None, required_food_in_kgs = 0):
        super().__init__(age_in_months, breed, required_food_in_kgs)
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += 0.5
'''
"""
class Animal:
    sound_by_animal=""
    make_breathe=""
    feed_grow=0
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        if age_in_months !=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
        else:
            self._age_in_months=age_in_months
        if required_food_in_kgs <=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
        else:
            self._required_food_in_kgs=required_food_in_kgs
        self._breed=breed
        
    
    
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def breed(self):
        return self._breed
    
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    
    
    @classmethod
    def breathe(cls):
        print(cls.make_breathe)
    
    @classmethod
    def make_sound(cls):
        print(cls.sound_by_animal)
        
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs += self.feed_grow    
        
class Deer(Animal):
    sound_by_animal="Buck Buck"
    make_breathe="Breathe in air"
    feed_grow=2
    
class Lion(Animal):
    sound_by_animal="Roar Roar"
    make_breathe="Breathe in air"
    feed_grow=4
    
    
class Shark(Animal):
    sound_by_animal="Shark Sound"
    make_breathe="Breathe oxygen from water"
    feed_grow=8
    
class GoldFish(Animal):
    sound_by_animal="Hum Hum"
    make_breathe="Breathe oxygen from water"
    feed_grow=0.2
    

class Snake(Animal):
    sound_by_animal="Hiss Hiss"
    make_breathe="Breathe in air"
    feed_grow=0.5


class Zoo:
    pass
    #def __init__(self)
    
"""


class Animals:
    sound = ""
    breath = ""
    add_food = 0
    def __init__(self,age_in_months=0, breed=None, required_food_in_kgs=0):
        self._age_in_months = age_in_months
        self._breed = breed
        self._required_food_in_kgs = required_food_in_kgs
        
        if self._age_in_months >= 10:
            raise ValueError(f'Invalid value for field age_in_months: {self._age_in_months}')
        if self._required_food_in_kgs <= 0:
            raise ValueError(f'Invalid value for field required_food_in_kgs: {self._required_food_in_kgs}')
        
    def grow(self):
        self._required_food_in_kgs += self.add_food
        self._age_in_months += 1
    
    @classmethod    
    def make_sound(cls):
        print(cls.sound)
    
    @property
    def age_in_months(self):
        return self._age_in_months
        
    @property
    def breed(self):
        return self._breed
        
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
        
        
class land_animals:
    @classmethod
    def breathe(cls):
        print('Breathe in air')
    
class water_animals: 
    @classmethod    
    def breathe(cls):
        print("Breathe oxygen from water")
    
       
class Hunting:
    animal = ""
    def hunt(self,zoo):
        c=0
        for i in zoo.animals_list:
            if type(i).__name__ == self.animal[0]:
                zoo.animals_list.remove(i)
                c=1
                break
        if c==0:
            print(f'No {self.animal[1]} to hunt')
        
    
class Deer(Animals,land_animals):
    sound = "Buck Buck"
    add_food = 2

class Lion(Animals,land_animals,Hunting):
    sound = "Roar Roar"
    add_food = 4
    animal = ["Deer","deers"]
    
class Shark(Animals,water_animals,Hunting):
    sound = "Shark Sound"
    add_food = 8
    animal = ["GoldFish","GoldFish"]
    
class GoldFish(Animals,water_animals):
    sound = "Hum Hum"
    add_food = 0.2

class Snake(Animals,land_animals,Hunting):
    sound = "Hiss Hiss"
    add_food = 0.5
    animal = ["Deer","deers"]

class Zoo:
    total_animals = []
    def __init__(self,reserved_food_in_kgs=0):
        self.animals_list = []
        self._reserved_food_in_kgs = reserved_food_in_kgs
        
    @property
    def reserved_food_in_kgs(self):
        return  self._reserved_food_in_kgs
        
        
    def add_food_to_reserve(self,food):
        self._reserved_food_in_kgs += food
        
    def add_animal(self,animale_obj):
        self.animals_list.append(animale_obj)
        Zoo.total_animals.append(animale_obj)
        
    def count_animals(self):
        return (len(self.animals_list))
        
    def feed(self,obj):
        
        if self._reserved_food_in_kgs != 0:
            self._reserved_food_in_kgs -= obj.required_food_in_kgs
            obj.grow()
        else:   
            self._reserved_food_in_kgs = 0
            
            
    @classmethod        
    def count_animals_in_all_zoos(cls):
        return (len(cls.total_animals))
        
    @staticmethod    
    def count_animals_in_given_zoos(zoo_list):
        count = 0
        for i in zoo_list:
            count += i.count_animals()
            
        return count


"""    
zoo = Zoo()
national = Zoo()
zoo.count_animals()
zoo.add_food_to_reserve(10000000)
print(zoo.reserved_food_in_kgs)
gold_fish = GoldFish(age_in_months=1, breed="Nemo", required_food_in_kgs=0.5)
national.add_animal(gold_fish)
zoo.feed(gold_fish)
zoo.add_animal(gold_fish)
print(zoo.reserved_food_in_kgs)
print(gold_fish.age_in_months)
zoo.add_animal(gold_fish)
zoo.add_animal(gold_fish)
zoo.count_animals()
print(Zoo.count_animals_in_given_zoos([national]))
lion = Lion(age_in_months=1, breed="African Lion", required_food_in_kgs=15)
national.add_animal(lion)
lion.hunt(national)
"""





