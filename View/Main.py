from Controls import *

welcome()   
while True:
    response = showMenu()
    
    if response == 1:
        response = menuP()
        if response == 4:
            continue
        elif response == 1:
            invLoan()
            continue
        elif response == 2:
            houseLoan()
            continue
        elif response == 3:
            vehicleLoan()
            continue
        
    
    elif response == 2:
        response = menuC()
        if response == 3:
            continue
        elif response == 1:
            registerSA()
            continue
        elif response == 2:
            registerCA()
            continue
        else:
            break 
    
    elif response == 3:
        registerEmp()
        continue
    
    elif response == 4:
        response = menuS()
        if response == 1:
            searchClient()
            continue
        elif response == 2:
            searchEmployee()
            continue
        else:
            continue
        
    elif response == 5:
        response = menuUp()
        if response == 1:
            updateClient()
            continue
        elif response == 2:
            updateEmployee()
            continue
        else:
            continue
    else: 
        break


    




