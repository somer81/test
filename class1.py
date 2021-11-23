class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname= lname
    def isim(self):
        print(self.fname, self.lname)

class Student(Person):
    def __init__(self,fname,lname,ogrno,gradYear):
        super().__init__(fname,lname)
        self.ogrno = ogrno
        self.gradYear = gradYear

    def isim(self):
        print(self.fname, self.lname,self.ogrno,self.gradYear)

p1 = Person("Mehmet","Tekin") # Başlangıçta otomatik olarak ilk değerler atanır

s1 = Student("Ayşe","Canikli",34234324,2022)

s1.isim()
print(s1.ogrno, s1.gradYear)
p1.isim()


