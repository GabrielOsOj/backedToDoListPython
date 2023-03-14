# lista de tareas api it 1

base_de_datos = {}

# diccionarios con opciones
menu_principal={1:"crear tarea",2:"editar tarea",3:"eliminar tarea",4:"salir del programa"}

menu_crear={1:"volver al menu principal",2:"salir"}


# funciones del crud

def ver_tareas():
	if(len(base_de_datos)==0):
		print("no hay tareas para mostrar")
	else:
     
		print("Lista de tareas\n-----------------------------\n|Tarea |Descripcion |Completa")
		for tarea in base_de_datos.items():
			print("|"+str(tarea[0])+"|"+str(tarea[1])+"|")
     
		


def crear_tarea():
	print("ingrese un titulo para la tarea")
	titulo=input()
    
	print("ingrese la tarea, maximo 30 caracteres")
	tarea = input()
	base_de_datos[titulo]=tarea
	print("la tarea: ",titulo," se guardo exitosamente!")
    
    
    
	while(True):
		try:	
			mostrar_opciones(menu_crear)

			seleccion_usuario=int(input())

			if(seleccion_usuario==1):			
				break
			elif(seleccion_usuario==2):
				crear_tarea()
			else:
				print("opcion invalida!")
				continue
		except:
			print("ingrese un valor numerico")
    
    
    
def editar_tarea():
    pass

def eliminar_tarea():
    pass
    
    
def mostrar_opciones(menu):
    
	for opcion in menu.items():
		print(opcion[0],":",opcion[1])



# main while
print("Bienvenido, seleccione una opcion:\n")


while(True):
	ver_tareas()
	mostrar_opciones(menu_principal)
	seleccion_usuario=int(input())


	match seleccion_usuario:
				
		case 1 :
			crear_tarea()
		case 2 :
			editar_tarea()
		case 3:
			eliminar_tarea()
		case 4:
			print("gracias por usar usarme :D")
			break
		case _:
			print("opcion no valida!")
			mostrar_opciones(menu_principal)
			continue
			



	 
    

