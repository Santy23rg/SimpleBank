BDClient = {}
BDLoan = {}
BDAccount = {}
BDEmployee = {}
contClient = 0
contLoan = 0
contAccount = 0
contEmployee = 0


def addClient(Person):
    global contClient
    contClient = contClient+1
    try:
        BDClient.update({
            "Client"+str(contClient): {
                "id" : Person.getId(),
                "name" : Person.getName(),
                "lastName" : Person.getLastName(),
                "age" : Person.getAge(),
                "dob" : Person.getDob(),
                "apDate" : Person.getApDate()
            }
        })
    
        return f"--------El cliente se registro correctamente--------"
    except:
        return f"¡¡¡Hubo un inconveniente con el registro!!! intentelo mas tarde"

def addEmployee(Person):
    global contEmployee
    contEmployee = contEmployee+1
    try:
        BDEmployee.update({
            "Employee"+str(contEmployee): {
                "id" : Person.getId(),
                "name" : Person.getName(),
                "lastName" : Person.getLastName(),
                "age" : Person.getAge(),
                "dob" : Person.getDob(),
                "apDate" : Person.getApDate()
            }
        })
    
        return f"--------El empleado se registro correctamente--------"
    except:
        return f"¡¡¡Hubo un inconveniente con el registro!!! intentelo mas tarde"
    
def addLoan(Loan):
    global contLoan
    contLoan = contLoan+1
    try:
        BDLoan.update({
            "Loan"+str(contLoan): {
                "idLoan" : Loan.getIdService(),
                "idClient" : Loan.getIdClient(),
                "type" : Loan.getType(),
                "value" : Loan.getValue(),
            }
        })
    
        return f"--------El prestamo se ingreso correctamente--------"
    except:
        return f"¡¡¡Hubo un inconveniente con el registro del prestamo!!! intentelo mas tarde"

def addAccount(Account):
    global contAccount
    contAccount = contAccount+1
    try:
        BDAccount.update({
            "Loan"+str(contLoan): {
                "idLoan" : Account.getIdService(),
                "idClient" : Account.getIdClient(),
                "type" : Account.getType(),
            }
        })
    
        return f"--------La cuenta se ingreso correctamente--------"
    except:
        return f"¡¡¡Hubo un inconveniente con el registro del prestamo!!! intentelo mas tarde"

def searchClient(id):
    val = 0
    for key, value in BDClient.items():
        if value["id"] == id:
            for k, v in BDAccount.items():
                if v["idClient"] == id:
                    service = v["type"]
            
            for k, v in BDLoan.items():
                if v["idClient"] == id:
                    service = v["type"]
                    val = v["value"]
            
            response = f"""\n   ID: {value["id"]}\n   Nombre: {value["name"]} {value["lastName"]}\n   Fecha de Nacimiento: {value["dob"]}\n   Fecha de Solicitud: {value["apDate"]}\n   Tipo de servicio: {service}\n"""
            
            if val != 0:
                response = response + f"   Valor: {val}"
            
            return response

def searchEmployee(id):
    for key, value in BDEmployee.items():
        if value["id"] == id:
            
            response = f"""\n   ID: {value["id"]}\n   Nombre: {value["name"]} {value["lastName"]}\n   Fecha de Nacimiento: {value["dob"]}\n   Fecha de Ingreso: {value["apDate"]}\n"""
            
            return response

def updateClient(id, Person=None):
    for key, value in BDClient.items():
        if value["id"] == id:
            if Person is not None:
                BDClient[key]["id"] = Person.getId()
                BDClient[key]["name"] = Person.getName()
                BDClient[key]["lastName"] = Person.getLastName()
                BDClient[key]["age"] = Person.getAge()
                BDClient[key]["dob"] = Person.getDob()

                for k, v in BDLoan.items():
                    if v["idClient"] == id:
                        BDLoan[k]["idClient"] = Person.getId()
                
                for k, v in BDAccount.items():
                    if v["idClient"] == id:
                        BDAccount[k]["idClient"] = Person.getId()
            
                return f"--------El cliente se actualizo correctamente--------"
            else:
                return True

def updateEmployee(id, Person=None):
    for key, value in BDEmployee.items():
        if value["id"] == id:
            if Person is not None:
                BDEmployee[key]["id"] = Person.getId()
                BDEmployee[key]["name"] = Person.getName()
                BDEmployee[key]["lastName"] = Person.getLastName()
                BDEmployee[key]["age"] = Person.getAge()
                BDEmployee[key]["dob"] = Person.getDob()

                
                return f"--------El Empleado se actualizo correctamente--------"
            else:
                return True
