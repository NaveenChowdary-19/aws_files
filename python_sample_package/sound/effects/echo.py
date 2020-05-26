"""The module echo

This is the "echo" module, providing some useless functions!
"""


a=10
b=9
def add(a,b):
    return a+b
    
c=add(a,b)
print(c,"Addition")

def sub(a,b):
    return a-b
    
d=sub(a,b)
print("Subtraction",d)

def print_echo():
    from.reverse import reverse_sound
    from sound.filters.equalizer import print_equi
    from..filters.equalizer import print_equi
    print("Prinnt Naeeeennnnn")
    reverse_sound()
    print_equi()

print("Module echo.py has been loaded!")
print_echo()