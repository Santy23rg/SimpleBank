from abc import ABC, abstractmethod
from BD import *

#Clase abstracta padre
class Person(ABC):
    def __init__(self, id,name, lastName, age, dob):
        self.__id = id
        self.__name = name
        self.__lastName = lastName
        self.__age = age
        self.__dob = dob
        
    def getName(self):
        return self.__name
    
    def getLastName(self):
        return self.__lastName
    
    def getId(self):
        return self.__id
    
    def getAge(self):
        return self.__age
    
    def getDob(self):
        return self.__dob
    
    def setName(self, name):
        self.__name = name
        
    def setLastName(self, lastName):
        self.__lastName = lastName
        
    def setId(self, id):
        self.__id = id
        
    def setAge(self, age):
        self.__age = age
        
    def setDob(self, dob):
        self.__dob = dob
        
        
    
    
