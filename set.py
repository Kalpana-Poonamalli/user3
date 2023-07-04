#Program to demonstrate sets in python- Un-ordered collection with no duplicates
s1={1,'a',3.5};
s2=set(["hello",4,'hi',4.7]);
print(s1)
print(s2)
#add a single element to the existing set
s1.add(4)
print(s1)
s1.add('a')
#add multiple elements or set to the existing set
s1.update(s2)
print(s1)
s1.update(['g','h',5])
print(s1)
#remove an element from set
s1.remove(1)
print(s1)
