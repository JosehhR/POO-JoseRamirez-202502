#Autor: Jose Luis Ramirez
#Estos son los primeros ejercicios del curso:

#1.Ejecute una entrada de texto e imprima
		
print("_______________________________")
print("Hola Mundo..")
print("_______________________________")
print ("1. Ejecute una entrada de texto e imprima")
print("_______________________________")
name=input("digite su nombre: ")
age=input("digite su edad: ")
print("_______________________________")
print("su nombre es: ", name, "\nSu edad es: ", age)
print("_______________________________")

#2. Realizar las tablas de multiplicar de un numero ingresado

def mTable(n, limit):
	for i in range (limit):
		print(f"{i+1} X {n} = {n*(i+1)}")
	return i
print ("2. Realizar las tablas de multiplicar del numero que usted ingrese")
print("_______________________________")
n=input("digite un numero para ver sus tablas de multiplicar: ")
i=input("digite hasta que numero quiere ver sus tablas de multiplicar: ")
print("")
mTable(int(n), int(i))
print("_______________________________")

#3. utilizando una funcion obtenga el numero factorial de un numero dado

def fact(n):
	r=1
	for i in range (n):
		r=r*(i+1)
	return r
print ("3. utilizando una funcion obtenga el numero factorial de un numero dado")
print("_______________________________")
n=input("digite un numero para ver su factorial: ")
r=fact(int(n))
print(f"el factorial de {n} es {r}")








