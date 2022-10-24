#Tomando en cuenta que los numeros telefonicos de Guatemala estan conformados por 8 digitos 
#y el primer dijito no puede ser 0, 1, 8 o 9 
#¿cuantos numeros telefonicos pares pueden existir en Guatemala?

# al primer digito le restamos los 4 que no pueden ser utilizados 0, 1, 8 o 9 = 6
print("ingrese el primer digito: ")
n1 = float(input())
print("ingrese el segundo digito: ")
n2 = float(input())
print("ingrese el tercer digito: ")
n3 = float(input())
print("ingrese el cuarto digito: ")
n4 = float(input())
print("ingrese el quinto digito: ")
n5 = float(input())
print("ingrese el sexto digito: ")
n6 = float(input())
print("ingrese el septimo digito: ")
n7 = float(input())
print("ingrese el octavo digito: ")
n8 = float(input())
#ya que tienen que ser resukltados pares a los 10 le restamos 5 a los digitos 2,3,4,5,6,7,8 = 5 

mult = n1 * n2 * n3 * n4 * n5 * n6 *n7 * n8

print("los numeros telefonicos pares que pueden existir en Guatemala son: ",mult)
