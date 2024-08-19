from abc import ABC, abstractmethod
import random
from BD import *

class Service(ABC):
    def __init__(self, typeService, idClient):
        self.__idService = idClient + str(random.randint(100,999))
        self.__typeService = typeService
        self.__idClient = idClient
    
    def getIdService(self):
        return self.__idService
    
    def getType(self):
        return self.__typeService
    
    def getIdClient(self):
        return self.__idClient
    
    
        
