import os as system

# lista de tareas api it 1
base_de_datos=[]

# diccionarios con opciones
menu_principal={0:"alternar estado",1:"crear tarea",2:"editar tarea",3:"eliminar tarea",4:"salir del programa"}

menu_crear={1:"crear otra tarea",2:"volver al menu principal"}

menu_eliminar={1:"cancelar",2:"eliminar"}

# funciones auxiliares
def limpiar_consola():
    system.system("cls")


# funciones del crud
def alternar_tarea():
    
	if(len(base_de_datos)==0):
		print("No hay tareas para alternar")
		print("Enter. Regresar")
		input()
		return;
    
	contador=1
	for i in base_de_datos:
		print(str(contador)+". "+i[0])
		contador+=1
    
	try:
		seleccion_usuario=int(input("Ingrese la tarea a alternar, 0 para volver atras\n"))-1
		
		if(seleccion_usuario==-1):
			return

		base_de_datos[seleccion_usuario][2]="completa" if base_de_datos[seleccion_usuario][2]=="incompleta" else "incompleta"
		limpiar_consola()
  
	except:
		limpiar_consola()
		print("\033[1;41m"+" opcion no valida "+"\033[0m")
		alternar_tarea()
	
	return


def ver_tareas():
	print("======================== \033[47m Lista de tareas \033[0m ========================\n|Tarea\t\t|Descripcion\t\t\t\t|Estado")
 
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

			color_completa_incompleta=""
  
			if tarea[2]=="completa":
				color_completa_incompleta="\033[1;42m"+" completa "+"\033[0m"
			else:
				color_completa_incompleta="\033[1;41m"+" incompleta "+"\033[0m"


			print("|"+str(tarea[0])+str(espacios[0])+"|"+str(tarea[1])+str(espacios[1])+"|"+color_completa_incompleta+str(espacios[2]))
     
def crear_tarea():
	tarea=["nueva tarea","descripcion",""]

	# print("ingrese un titulo para la tarea (maximo 15 caracteres)")
	nuevoTitulo=input("ingrese un titulo para la tarea (maximo 15 caracteres)\n")[0:15]
    
	nuevaDescripcion = input("ingrese la tarea, maximo 30 caracteres\n")[0:30]
 
	tarea[0]="sin titulo" if nuevoTitulo=="" else nuevoTitulo
	tarea[1] ="sin descripcion" if nuevaDescripcion=="" else nuevaDescripcion
	tarea[2]="incompleta"
	
	base_de_datos.append(tarea)
	limpiar_consola()
	print("\033[1;42m"+"la tarea: ",tarea[0]," se guardo exitosamente!"+"\033[0m")
	
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
				print("\033[1;41"+"seleccione una opcion valida!"+"\033[0m")
				
				      			
		except:
			print("\033[1;42m"+"ingrese un valor numerico"+"\033[0m")
		break

    
def editar_tarea():
    
	if(len(base_de_datos)==0):
		print("No hay tareas para editar")
		print("Enter. Regresar")
		input()
		return;

	contador=1
	for i in base_de_datos:
		print(str(contador)+". "+i[0])
		contador+=1
   
	try:
		print("Ingrese el indice de la tarea que desea editar")
		seleccion_usuario=int(input())

		if seleccion_usuario>len(base_de_datos):
			limpiar_consola()
			print("\033[1;41m"+"Opcion invalida!"+"\033[0m")
			editar_tarea()
		
		print("\033[1;43m"+"Titulo actual: "+base_de_datos[seleccion_usuario-1][0]+"\nDescripcion actual: "+base_de_datos[seleccion_usuario-1][1]+"\033[0m")
  
		print("ingrese nuevo titulo, deje en blanco para no editar")
		nuevo_titulo=input()

		print("ingrese nueva descripcion, deje en blanco para no editar")
		nueva_descripcion=input() 

		base_de_datos[seleccion_usuario-1][0]=nuevo_titulo if nuevo_titulo != "" else base_de_datos[seleccion_usuario-1][0]
		base_de_datos[seleccion_usuario-1][1]=nueva_descripcion if nueva_descripcion != "" else base_de_datos[seleccion_usuario-1][1]
			
		print("\033[1;42m"+"La tarea se modifico correctamente!"+"\033[0m")
		input()
		return

	except:
		limpiar_consola()
		print("\033[1;41m"+"¡Ingrese una opcion valida!"+"\033[0m")
		editar_tarea()



def eliminar_tarea():
    
	if(len(base_de_datos)==0):
		print("No hay tareas para borrar")
		print("Enter. Regresar")
		input()
		return;
    
	try:
		contador=1
		for i in base_de_datos:
			print(str(contador)+". "+i[0])
			contador+=1
		
		print("Ingrese el numero de la tarea que quiere eliminar, escriba 0 para volver atras")
		seleccion_usuario=int(input())

		if(seleccion_usuario==0):
			return		
  
		base_de_datos.pop(seleccion_usuario-1)
		print("\033[42m"+"la tarea se elimino correctamente"+"\033[0m")
		input()
		limpiar_consola()
		return

	except:
			limpiar_consola()
			print("Ingrese un valor valido!")
			eliminar_tarea()		
   

def mostrar_opciones(menu):
    
	for opcion in menu.items():
		print(opcion[0],":",opcion[1])


# main while
print("Bienvenido, seleccione una opcion:\n")

while(True):
	try:
		ver_tareas()
		print("===================================================================")
		mostrar_opciones(menu_principal)
		seleccion_usuario=int(input())
		limpiar_consola()

		match seleccion_usuario:
      
			case 0:
				alternar_tarea()
				limpiar_consola()
			case 1 :
				crear_tarea()
				limpiar_consola()
			case 2 :
				editar_tarea()
				
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

	except:
		print("\033[1;41m"+"ingrese una opcion valida"+"\033[0m")
  

			