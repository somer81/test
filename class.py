class Person:
  def __init__(self, name, age, surname):
    self.name = name
    self.age = age
    self.surname = surname

  def myName(self):
      print(self.name + " " + self.surname)
    
p1 = Person("John", 36, "Micheal")
p2 = Person("Hakan", 32, "Tekin")

print(p1.name)
print(p1.age)
print(p1.surname)
print(p2.name + " " + str(p2.age) + " " + p2.surname)
p1.myName()
