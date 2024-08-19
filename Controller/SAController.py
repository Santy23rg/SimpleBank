from ServiceController import *

class SAController(ServiceController):
    
    def register(account):
        response = addAccount(account)
        return response
    
    
