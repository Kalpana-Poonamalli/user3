class A:
    def __init__(self,h):
        self.house=h;
    def displayAProperties(self):
        print('A house is:'+self.house);
        
class B:
    def __init__(self,c):
        self.car=c;
    def displayBProperties(self):
        print('B car is:'+self.car);
        
class C(A,B):
    def __init__(self,h,c,b):
        self.bike=b;
        super().__init__(h);
        super().__init__(c);
        def displayCProperties(self):
        print('C house is:'+self.house);    
        print('C car is:'+self.car);    
        print('C bike is:'+self.bike);
        
sub=C('duplex house','honda city','KTM');
sub.displayCProperties();
sub.displayBProperties();        
sub.displayAProperties();