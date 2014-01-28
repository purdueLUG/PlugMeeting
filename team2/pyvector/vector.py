#!/usr/bin/python

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __str__(self):
        return "(%f, %f, %f)"%(self.x,self.y,self.z)

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
print v1.add(v2)

