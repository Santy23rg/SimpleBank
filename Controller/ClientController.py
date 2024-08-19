from PersonController import *

class ClientController(PersonController):
    
    def register(Person):
        response = addClient(Person)
        return response

    def search(id):
        response = searchClient(id)
        if response:
            return response
        else:
            return "No hay ningun resultado"  
          
    def update(id, Person=None):
        if Person is None:
            response = updateClient(id)
            return response
        else:
            response = updateClient(id, Person)
            return response
        
        