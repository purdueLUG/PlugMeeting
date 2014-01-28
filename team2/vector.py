#!/usr/bin/python

from vectorcross import *
from  vectordot import *

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)

    def __str__(self):
        return "(%f, %f, %f)"%(self.x,self.y,self.z)
    
    def cross(self,other):
        temp = CrossProduct(self.x, self.y,self.z,other.x, other.y, other.z)
        return Vector(temp[0], temp[1], temp[2])

    def dot(self, other):
        temp = dot([self.x,self.y,self.z],[other.x,other.y,other.z])
        return Vector(temp[0], temp[1], temp[2])

print v1.add(v2)
print v1.cross(v2)
print v1.dot(v2)
