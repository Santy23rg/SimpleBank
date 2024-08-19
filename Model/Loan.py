from Service import * 

class Loan(Service):
    def __init__(self, typeService, idClient, val):
        super().__init__(typeService, idClient)
        self.__val = val
        
    def getValue(self):
        return self.__val
    