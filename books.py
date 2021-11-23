class Yazar:
    pass
    
class Book:
    def __init__(self,ad,yazar,tur,sayfa):
        self.ad = ad
        self.yazar = yazar
        self.tur = tur
        self.sayfa = sayfa

    def kitapBilgi(self):
        print(self.ad + "\n" + self.yazar)
        print(self.tur)

class Ansiklopedi(Book):
    def __init__(self,ad,yazar,tur,sayfa,cilt):
        super().__init__(ad,yazar,tur,sayfa)
        self.cilt = cilt
    def kitapBilgi(self):
        super().kitapBilgi()
        print(self.cilt)
    


book1 = Book("Anayurt Oteli", "Yusuf Atılgan","Psikoloji",300)
book1.kitapBilgi()
print("---------------")
ans1 = Ansiklopedi("Larausse","Anonim","Genel",10000,10)
ans1.kitapBilgi()




    
