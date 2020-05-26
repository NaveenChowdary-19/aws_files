class PokeMon:
    #sound = "hello"
    def __init__(self,name = None,level = 1,master = None  , sound = ""):
        self._name = name
        self._level = level
        self._master = None
        self.sound= sound
    @classmethod  
    def makesound(self):
        try:
            self.sound
        except:
            return "No sound"
    
pokemon =PokeMon()

print(pokemon.makesound())
        