from Person import *

class Client(Person):
    def __init__(self, id, name, lastName, age, dob, apDate=""):
        super().__init__(id, name, lastName, age, dob)
        self.__apDate = apDate
        self.__dob = dob
    
    def getDob(self):
        return self.__dob
    
    def getApDate(self):
        return self.__apDate
    
