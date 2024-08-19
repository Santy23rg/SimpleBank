import datetime
from pathlib import Path
import sys

# Obtener la ruta del directorio actual
current_dir = Path(__file__).parent

# Construir la ruta relativa
model_path = current_dir / '../Model'
controller_path = current_dir / '../Controller'

# Importar el módulo
sys.path.append(str(model_path))
sys.path.append(str(controller_path))

from ClientController import *
from Client import *
from EmployeeController import *
from Employee import *
from LoanController import *
from Loan import *
from SAController import *
from SavingAccount import *
from CAController import *
from CurrentAccount import *

# Form de ingreso de prestamos 
def inputLoan(typeLoan):
    while True:    
        try:
            id = input("Ingrese su numero de identificacion: ")
            name = input("Ingrese su nombre: ")    
            lastName = input("Ingrese su apellido: ")     
            dob = input("Ingrese la fecha de su nacimiento (YYYY-MM-DD): ")
            val = input("Ingrese el valor del prestamo a solicitar: ")
            apDate = datetime.date.today()   
            dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
            dif = apDate-dob
            age = dif.days // 365
            break
        except:
            print("\n¡Ingresaste algun dato de forma erronea!, ingrese los datos de forma correcta por favor\n")   
            continue 
        
    loan = Loan(typeLoan, id, val)
    client = Client(id,name,lastName, age, dob, apDate)
    response = ClientController.register(client)
    print("\n" + response + "\n")
    response = LoanController.register(loan)
    print("\n" + response + "\n")
    print("La solicitud del prestamo se ingreso correctamente \n")

def inputAccount(typeAccount):
    while True:    
        try:
            id = input("Ingrese su numero de identificacion: ")
            name = input("Ingrese su nombre: ")    
            lastName = input("Ingrese su apellido: ")     
            dob = input("Ingrese la fecha de su nacimiento (YYYY-MM-DD): ")
            apDate = datetime.date.today()   
            dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
            dif = apDate-dob
            age = dif.days // 365
            break
        except:
            print("\n¡Ingresaste algun dato de forma erronea!, ingrese los datos de forma correcta por favor\n")   
            continue 
        
    client = Client(id,name,lastName, age, dob, apDate)
    response = ClientController.register(client)
    print("\n" + response + "\n")
    if typeAccount == "Cuenta de Ahorros":
        account = SavingAccount(typeAccount, id)
        response = SAController.register(account)
    else:
        account = CurrentAccount(typeAccount, id)
        response = CAController.register(account)
    print("\n" + response + "\n")
    print(f"Cuenta creada correctamente\n")
    
def inputEmployee():
    while True:    
        try:
            id = input("Ingrese numero de identificacion del empleado: \n")
            name = input("Ingrese el nombre: \n")    
            lastName = input("Ingrese su apellido: \n")     
            dob = input("Ingrese la fecha de su nacimiento (YYYY-MM-DD): \n")
            apDate = datetime.date.today()   
            dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
            dif = apDate-dob
            age = dif.days // 365
            break
        except:
            print("\n¡Ingresaste algun dato de forma erronea!, ingrese los datos de forma correcta por favor\n")   
            continue 
    
    Emp = Employee(id,name,lastName, age, dob, apDate)
    response = EmployeeController.register(Emp)
    print("\n" + response + "\n")
    
#TITULOS---------------------------------------------------

def welcome():
    print("-"*50 + "\n"
          "**"+" "*16 + "WELCOME TO ABC" + " "*16 + "**" + "\n" +
          "-"*50 + "\n")

def titleInv():
    print("-"*50 + "\n"
          "**"+" "*11 + "Solicitud Libre inversión" + " "*10 + "**" + "\n" +
          "-"*50 + "\n")

def titleHouse():
    print("-"*50 + "\n"
          "**"+" "*14 + "Solicitud Vivienda" + " "*14 + "**" + "\n" +
          "-"*50 + "\n")

def titleVehicle():
    print("-"*50 + "\n"
          "**"+" "*14 + "Solicitud Vehiculo" + " "*14 + "**" + "\n" +
          "-"*50 + "\n")

def titleSA():
    print("-"*50 + "\n"
          "**"+" "*9 + "Solicitud Cuenta de Ahorros" + " "*10 + "**" + "\n" +
          "-"*50 + "\n")

def titleCA():
    print("-"*50 + "\n"
          "**"+" "*10 + "Solicitud Cuenta Corriente" + " "*10 + "**" + "\n" +
          "-"*50 + "\n")

def titleEmp():
    print("-"*50 + "\n"
          "**"+" "*13 + "Registro de Empleado" + " "*13 + "**" + "\n" +
          "-"*50 + "\n")

def titleUpdate():
    print("-"*50 + "\n"
          "**"+" "*12 + "Actualizacion de Datos" + " "*12 + "**" + "\n" +
          "-"*50 + "\n")
#-------------------------------------------------------

#MENUS---------------------------------------------------------

#Menu principal
def showMenu():
    print("\n ¿Que quieres realizar? \n")
    while True:
        try:
            response = int(input("1. Solicitar prestamo \n2. Abrir cuenta \n3. Registrar Empleado \n4. Consultar \n5. Actualizar Informacion \n6. Finalizar Tramite\n"))
            if str(response) in "123456":
                break
            else:
                print("¡Porfavor ingrese una opcion valida! \n")
                continue
            
        except:
            print("¡Porfavor ingrese una opcion valida! \n")
        
    return response

#Menu cuentas
def menuC():
    print("\n ¿Que tipo de cuenta desea solicitar?")
    while True:
        try:
            response = int(input("1. Cuenta de Ahorros \n2. Cuenta Corriente \n3.Volver al menu principal \n"))
            if str(response) in "123":
                break
            else:
                print("¡Porfavor ingrese una opcion valida! \n")
                continue
            
        except:
            print("¡Porfavor ingrese una opcion valida! \n")
        
    return response
#Menu de busquedas
def menuS():
    print("\n ¿Que deseas consultar?")
    while True:
        try:
            response = int(input("1. Buscar Cliente \n2. Buscar Empleado \n3.Volver al menu principal \n"))
            if str(response) in "123":
                break
            else:
                print("¡Porfavor ingrese una opcion valida! \n")
                continue
            
        except:
            print("¡Porfavor ingrese una opcion valida! \n")
        
    return response

#Menu Actualizacion
def menuUp():
    print("\n ¿Que deseas actualizar?")
    while True:
        try:
            response = int(input("1. Cliente \n2. Empleado \n3.Volver al menu principal \n"))
            if str(response) in "123":
                break
            else:
                print("¡Porfavor ingrese una opcion valida! \n")
                continue
            
        except:
            print("¡Porfavor ingrese una opcion valida! \n")
        
    return response

#Menu prestamos
def menuP():
    print("\n ¿Que tipo de prestamos desea solicitar?")
    while True:
        try:
            response = int(input("1. Libre Inversion \n2. Vivienda \n3. Vehiculo \n4. Volver al menu principal \n"))
            if str(response) in "1234":
                break
            else:
                print("¡Porfavor ingrese una opcion valida! \n")
                continue
            
        except:
            print("¡Porfavor ingrese una opcion valida! \n")
        
    return response

#-----------------------------------------------------------------

#REGISTROS --------------------------------------------------------

#Registro de solicitud de libre inversion
def invLoan():
    typeLoan = "Prestamo Libre Inversion"
    titleInv()
    inputLoan(typeLoan)
    
#Registro de solicitud de vivienda
def houseLoan():
    typeLoan = "Prestamo Vivienda"
    titleHouse()
    inputLoan(typeLoan)
    
#Registro de solicitud de vehiculo
def vehicleLoan():
    typeLoan = "Prestamo Vehiculo"
    titleVehicle()
    inputLoan(typeLoan)
    
def registerSA():
    typeAccount = "Cuenta de Ahorros"
    titleSA()
    inputAccount(typeAccount)

def registerCA():
    typeAccount = "Cuenta Corriente"
    titleCA()
    inputAccount(typeAccount)
    
def registerEmp():
    titleEmp()
    inputEmployee()

#---------------------------------------------------------

#Consultas------------------
def searchClient():
    id = input("Ingrese el id del cliente: ")
    response = ClientController.search(id)
    print(response)
    
def searchEmployee():
    id = input("Ingrese el id del empleado: ")
    response = EmployeeController.search(id)
    print(response)

def updateClient():
    titleUpdate()
    id = input("Ingrese el id del cliente que desea modificar: ")
    response = ClientController.update(id)
    if response:
        while True:    
            try:
                idAct = input("Ingrese su numero de identificacion: ")
                name = input("Ingrese su nombre: ")    
                lastName = input("Ingrese su apellido: ")     
                dob = input("Ingrese la fecha de su nacimiento (YYYY-MM-DD): ")
                apDate = datetime.date.today()   
                dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
                dif = apDate-dob
                age = dif.days // 365
                break
            except:
                print("\n¡Ingresaste algun dato de forma erronea!, ingrese los datos de forma correcta por favor\n")   
                continue
        
        client = Client(idAct,name,lastName, age, dob, apDate)
        response = ClientController.update(id, client)
        print("\n" + response + "\n")
    else:
        print("Lo siento, no hay resultados con ese numero de identificacion")

def updateEmployee():
    titleUpdate()
    id = input("Ingrese el id del empleado que desea modificar: ")
    response = EmployeeController.update(id)
    if response:
        while True:    
            try:
                idAct = input("Ingrese numero de identificacion del empleado: \n")
                name = input("Ingrese el nombre: \n")    
                lastName = input("Ingrese su apellido: \n")     
                dob = input("Ingrese la fecha de su nacimiento (YYYY-MM-DD): \n")
                apDate = datetime.date.today()   
                dob = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
                dif = apDate-dob
                age = dif.days // 365
                break
            except:
                print("\n¡Ingresaste algun dato de forma erronea!, ingrese los datos de forma correcta por favor\n")   
                continue 
            
        Emp = Employee(idAct, name, lastName, age, dob, apDate)
        response = EmployeeController.update(id, Emp)
        print("\n" + response + "\n")
    else:
        print("Lo siento, no hay resultados con ese numero de identificacion")