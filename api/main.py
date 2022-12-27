from request import *
import os

class Menu:
    def __init__():

        def limpiarpantalla():
            os.system('cls')

        
        print("====================MENU=================")
        print("= 1) Mostrar los empleados disponibles  =")
        print("= 2) Mostrar un empleado                =")
        print("= 3) Ingresar un nuevo empleado         =")
        print("= 4) Editar el nombre de un empleado    =")
        print("= 5) Eliminar un empleado               =")
        print("=========================================")
        
        op = int(input("Ingrese una de las opciones del Menù:  "))       
        limpiarpantalla()      
        if op == 1:           
            print("===============Todos Los Empleados ===============")
            u=solicitudes("http://localhost:5000/employees")
            u.get()
            input("========PRESIONE ENTER PARA CONTINUAR!========")
            limpiarpantalla()
            Menu.__init__()
        
        elif op == 2:
            id = int(input("Ingrese el id del empleado que desea mostrar: "))
            limpiarpantalla()
            print("""        
            =============Empleado Seleccionado============
            """)
            u=solicitudes("http://localhost:5000/employees")
            u.get_id(id)
            input("========PRESIONE ENTER PARA CONTINUAR!========")
            limpiarpantalla()
            Menu.__init__()
        elif op == 3:
            name = input("Ingrese el nombre del nuevo empleado: ")
            cargo = input("Ingrese el cargo del nuevo empleado: ")
            u=solicitudes("http://localhost:5000/employees")
            u.post(name,cargo)
            limpiarpantalla()            
            print("====================Empleado Ingresado========================")
            input("===========PRESIONE ENTER PARA VER LA NUEVA LISTA==========")
            u=solicitudes("http://localhost:5000/employees")
            u.post(name,cargo)
            input("========PRESIONE ENTER PARA CONTINUAR!========")
            limpiarpantalla()
            Menu.__init__()           
        elif op == 4:
            id = int(input("Ingrese el id del empleado que desea modificar: "))
            name = input("Ingrese el nuevo nombre del empleado: ")      
            u=solicitudes("http://localhost:5000/employees")
            u.put(id,name)
            limpiarpantalla()
            print("==================Empleado Modificado======================")
            u=solicitudes("http://localhost:5000/employees")
            u.get_id(id)
            input("========PRESIONE ENTER PARA CONTINUAR!========")
            limpiarpantalla()
            Menu.__init__()           
        elif op == 5:
            id = int(input("Ingrese el id del empleado que quiere eliminar: "))
            u=solicitudes("http://localhost:5000/employees")
            u.delete(id)
            input("========PRESIONE ENTER PARA CONTINUAR!========")
            limpiarpantalla()
            Menu.__init__()
        else:
            input("""
            ==============================================
            ====================ADIOS!====================
            ==============================================\n\n
            presione Enter\n----->
            """)
            limpiarpantalla()            
            pass
Menu.__init__()