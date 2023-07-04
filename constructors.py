#Program to demonstrate constructors-to initialise instance variables
class PythonTraining:
    def __init__(self,a,b):
        print('i am constructor method')
        self.pen=a;
        self.book=b;
    def display(self):
        print('my pen is '+self.pen);
        print('my book is '+self.book);
#Object Creation
x=PythonTraining('parker','white notebook');
x.display();
y=PythonTraining('Ronalds','Rule Notebook');
y.display();