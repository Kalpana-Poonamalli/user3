class A:
    def __init__(self,h,c):
        self.house=h;
        self.car=c;
    def displayAProperties(self):
        print('A house is :'+self.house);
        print('A car is:'+self.car);
class B(A):
    def __init__(self,h,c,b):
        self.bike=b;
        super().__init__(h,c);
    def displayBProperties(self):
        print('B house is :'+self.house);
        print('B car is :'+self.car);
        print('B bike is :'+self.bike);
class C(A):
    def __init__(self,h,c,f): 
        self.fridge=f;
        super().__init__(h,c);
    def displayCProperties(self):
        print('C house is :'+self.house);
        print('C car is :'+self.car);
        print('C fridge is :'+self.fridge); 
sub1=B('Duplex House','Honda City','KTM');
sub2=C('Duplex House','Honda City','Whirlpool'); 
sub1.displayAProperties();
sub1.displayBProperties();       
sub2.displayCProperties();