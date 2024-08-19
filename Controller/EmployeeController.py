from PersonController import *

class EmployeeController(PersonController):
    
    def register(Person):
        response = addEmployee(Person)
        return response

    def search(id):
        response = searchEmployee(id)
        if response:
            return response
        else:
            return "No hay ningun resultado"  
    
    def update(id, Person=None):
        if Person is None:
            response = updateEmployee(id)
            return response
        else:
            response = updateEmployee(id, Person)
            return response