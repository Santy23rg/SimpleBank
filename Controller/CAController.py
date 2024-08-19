from ServiceController import *

class CAController(ServiceController):
    
    def register(account):
        response = addAccount(account)
        return response
    
    def update():
        pass
    
    def search():
        pass