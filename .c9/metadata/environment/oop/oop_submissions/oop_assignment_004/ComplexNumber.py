{"filter":false,"title":"ComplexNumber.py","tooltip":"/oop/oop_submissions/oop_assignment_004/ComplexNumber.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":50,"column":111},"action":"insert","lines":["from math import sqrt","class ComplexNumber:","","    def __init__(self,real_part=0,imaginary_part=0):","       ","        if type(real_part)==str and type(imaginary_part)!=str:","            raise ValueError(\"Invalid value for real part\")","        else:","            self.real_part=real_part","        if type(imaginary_part)==str and type(real_part)!=str:","            raise ValueError(\"Invalid value for imaginary part\")","        else:","            self.imaginary_part=imaginary_part","        if type(real_part)==str and type(imaginary_part)==str:","            raise ValueError(\"Invalid value for real and imaginary part\")","        else:","            self.real_part=real_part","            self.imaginary_part=imaginary_part","            ","    def conjugate(self):","       return ComplexNumber(self.real_part,-self.imaginary_part)","    ","    def __eq__(self,other):","        return self.real_part==other.real_part and self.imaginary_part==other.imaginary_part       ","    ","    def __abs__(self):","        return round(sqrt(self.real_part**2+self.imaginary_part**2),3)","    def __add__(self,other):","        return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)","    def __sub__(self,other):","        return ComplexNumber(self.real_part-other.real_part,self.imaginary_part-other.imaginary_part)","    def __mul__(self, other):","        return ComplexNumber(self.real_part*other.real_part - self.imaginary_part*other.imaginary_part,","                     self.imaginary_part*other.real_part+ self.real_part*other.imaginary_part)","","    def __truediv__(self, other):","    ","        sr, si, ori, oi = self.real_part, self.imaginary_part,other.real_part, other.imaginary_part # short forms","        r = float(ori**2 + oi**2)","        return ComplexNumber((sr*ori+si*oi)/r, (si*ori-sr*oi)/r)","        ","        '''","        k=abs(other)","        self.real_part=self.real_part/k","        self.imaginary_part=self.imaginary_part/k","        other.real_part=other.real_part/k","        other.imaginary_part=-(other.imaginary_part)/k'''","        ","    ","    def __str__(self):        ","        return '{}{}{}i'.format(self.real_part,'+' if self.imaginary_part>=0 else '-',abs(self.imaginary_part))"],"id":1}],[{"start":{"row":40,"column":7},"end":{"row":47,"column":8},"action":"remove","lines":[" ","        '''","        k=abs(other)","        self.real_part=self.real_part/k","        self.imaginary_part=self.imaginary_part/k","        other.real_part=other.real_part/k","        other.imaginary_part=-(other.imaginary_part)/k'''","        "],"id":2}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":40,"column":7},"end":{"row":40,"column":7},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1587479531347,"hash":"30da145b51f62833f153a8de79b20325411d49a5"}