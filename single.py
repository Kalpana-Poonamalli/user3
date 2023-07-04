class GrandParent :
    def __init__(self,h):
        self.house=h;
    def displayGrandParentProperties(self) :
        print('grand parent house is:'+self.house);

class Parent(GrandParent) :
    def __init__(self,h,c) :
        self.car=c;
        super().__init__(h);
    def displayParentProperties(self):
        print('parent house is:'+self.house);
        print('parent car is :'+self.car);

sub1=Parent('Duplex House','Honda city');
sub1.displayParentProperties();
sub1.displayGrandParentProperties();