'''
в программе должны быть два класса и два объекта,
принадлежащих разным классам; один объект с помощью метода своего класса должен так или иначе обрабатывать данные другого объекта:
obj1.МЕТОД(obj2.СВОЙСТВО).
'''
class Triangle:
    leg1 = 5
    leg2 = 0
    hypotenuse = 9
    def findleg(self):
        self.leg2 = (self.hypotenuse**2 - self.leg1**2)**(1/2)

class Area:
    area = 0
    def findarea(self,leg1,leg2):
        self.area = leg1*leg2/2

tr1 = Triangle()
tr1.findleg()

plat = Area()
print("Leg 1 = "+ str(tr1.leg1))
print("Leg 2 = "+ str(tr1.leg2))
plat.findarea(tr1.leg1, tr1.leg2)
print("Area triangle = " + str(plat.area))
