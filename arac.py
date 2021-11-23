class Arac:
    def __init__(self, renk, kilo, motorHacim, model):
        self.renk = renk
        self.kilo = kilo
        self.motorHacim = motorHacim
        self.model = model
    def aracBilgi(self):
        print(self.model,self.motorHacim,self.kilo,self.renk)

class Otomobil(Arac):
    def __init__(self,renk, kilo, motorHacim, model, hiz, Ncap):
        super().__init__(renk, kilo, motorHacim, model)
        self.hiz = hiz
        self.Ncap = Ncap
    def aracBilgi(self):
        super().aracBilgi()
        print(self.hiz,self.Ncap)
    def maxHiz(self):
        return self.hiz + 20

a1 = Arac( "red",1800, 1500,2020)
a2 = Arac("white",1200, 1000,2004)

o1 = Otomobil("yellow",1200, 1300,2015, 260, 4)
a1.aracBilgi()
a2.aracBilgi()
o1.aracBilgi()
#print(o1.hiz,o1.Ncap)
print("Max Hız : " + str(o1.maxHiz()))


