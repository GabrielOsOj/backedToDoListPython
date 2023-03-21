import os as system

# lista de tareas api it 1
base_de_datos=[]

# diccionarios con opciones
menu_principal={1:"crear tarea",2:"editar tarea",3:"eliminar tarea",4:"salir del programa"}

menu_crear={1:"crear otra tarea",2:"volver al menu principal"}

menu_eliminar={1:"cancelar",2:"eliminar"}

# funciones del crud

def limpiar_consola():
    system.system("cls")

def salto_de_linea(cantidad):
    for i in range(cantidad):
        print("\n")

def ver_tareas():
	print("======================== \033[7m Lista de tareas \033[0m ========================\n|Tarea\t\t|Descripcion\t\t\t\t|Estado")
 
	if(len(base_de_datos)==0):
		print("no hay tareas para mostrar")
	else:

		for tarea in base_de_datos:
			
			espacios=["","",""]

			for i in range(15-len(tarea[0])):
				espacios[0]+=" "
			for i in range(39-len(tarea[1])):
				espacios[1]+=" "
			for i in range(10-len(tarea[2])):
				espacios[2]+=" "

			print("|"+str(tarea[0])+str(espacios[0])+"|"+str(tarea[1])+str(espacios[1])+"|"+str(tarea[2])+str(espacios[2]))
     
def crear_tarea():
	tarea=["nueva tarea","descripcion",""]

	print("ingrese un titulo para la tarea")
	tarea[0]=input()
    
	print("ingrese la tarea, maximo 30 caracteres")
	tarea[1] = input()
	tarea[2]="incompleta"
	
	# usar operador ternario 
	
 
	if(tarea==""):
		tarea="nueva tarea"
	
	if(tarea==""):
		tarea="descripcion"
 
	base_de_datos.append(tarea)
	limpiar_consola()
	print("la tarea: ",tarea[0]," se guardo exitosamente!")
	
	while(True):
		try:	
			mostrar_opciones(menu_crear)
			seleccion_usuario=int(input())
			
			if (seleccion_usuario==1):
				limpiar_consola()
				crear_tarea()
			elif(seleccion_usuario==2):
				break
			else:
				print("seleccione una opcion valida!")
				      			
		except:
			print("ingrese un valor numerico")
   
		break

    
def editar_tarea():
    pass

def eliminar_tarea():
	print("seleccione la tarea para eliminar")
	
	for i in base_de_datos.items():
		print(i)



def mostrar_opciones(menu):
    
	for opcion in menu.items():
		print(opcion[0],":",opcion[1])


# main while
print("Bienvenido, seleccione una opcion:\n")

while(True):
	ver_tareas()
	print("===================================================================")
	mostrar_opciones(menu_principal)
	seleccion_usuario=int(input())
	limpiar_consola()

	match seleccion_usuario:
				
		case 1 :
			crear_tarea()
			limpiar_consola()
		case 2 :
			editar_tarea()
			limpiar_consola()
		case 3:
			eliminar_tarea()
		case 4:
			limpiar_consola()
			print("gracias por usar usarme :D")
			break
		case _:
			print("opcion no valida!")
			mostrar_opciones(menu_principal)
			continue


			