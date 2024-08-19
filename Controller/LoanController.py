from ServiceController import *

class LoanController(ServiceController):
    
    def register(Loan):
        response = addLoan(Loan)
        return response
    
    def update(self):
        pass
    
    def search(self):
        pass
    