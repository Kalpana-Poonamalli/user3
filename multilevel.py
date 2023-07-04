class  GrandParent:
    def __init__(self,h):
        self.house=h;
    def displayGrandParentProperties(self):
        print('Grand parent house is:'+self.house);
class Parent(GrandParent):
    def __init__(self,h,c):
        self.car=c;
        super().__init__(h);
    def displayParentProperties(self):
        print('Parent house is:'+self.house);
        print('Parent car is:'+self.car);
class Child(Parent):
    def __init__(self,h,c,b):
        self.bike=b;
        super().__init__(h,c);
    def displayChildProperties(self):
        print('Child house is :'+self.house);
        print('Child car is :'+self.car);
        print('Child bike is:'+self.bike);
sub=Child('Duplex House','Honda City','Royal Enfield');
sub.displayChildProperties();
sub.displayParentProperties();
sub.displayGrandParentProperties();
    
      