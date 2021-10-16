print("Hola mundo") # print imprime en pantalla el mensaje que esta dentro de comillas
#en python no necesitas definir un tipo de dato solo basta con poner
#nombredevariable= dato   ejemplos
numero=18 #numero entero
decimal=1.3 #numero decimal
#una forma de imprimir variables es la siguiente
print("numero 1: {}  \nnumero 2: {}".format(numero,decimal)) #\n sirve para un salto de linea

numero2=2
#operaciones en python
suma= numero + decimal # + es para suma
resta= numero - decimal # - es para restar
multi= numero * decimal # * es para multiplicar
divi= numero / decimal # / es para dividir
pote= numero ** numero2 # ** es para potencia
divente= numero // decimal # // es para division entera
mod=numero % decimal # % es para modulo
numero+= 2 # += incrementa en este caso incrementa en dos unidades
inc=numero
numero-=4 # -= decrementa en este caso decrementa en cuatro unidades
dec=numero

print("suma: {}\nresta: {}\nmultiplicacion: {}".format(suma,resta,multi))

#una forma mas de imprimir variables 
print ("Division: ", divi)
print ("Potencia: ",pote)
print ("Division entera: ",divente)
print ("Modulo: ",mod)
print ("incremento: ",inc)
print ("Decremento", dec)

#Manejar textos
texto= "hola "
texto2= "GENTE"
print("Concatenanado: "+texto+" "+texto2)#concatena un texto con +
print("Texto multiplicado: "+texto*3)#multiplica un texto con *
print ("letras en gente: {}".format(len(texto2)))#len cuenta las letras de un texto
print("Texto en mayusculas: {}".format(texto.upper()))#.upper() cambia texto a mayusculas
minu=texto2.lower()#.lower() cambia texto a minusculas
print("texto en minusculas: ",minu)
arreglo=['tony','jorge','luis']#arreglo de strings
print("***".join(arreglo));#.join saca los elementos de un arreglo 
print("ejemplo split y soy tony que bien".split())#split convierte la cadena en arreglo

edad=input("Ingresa tu edad ")
num=input("Ingresa un numero ")#input recibe elementos por teclado 
#al escribir input todo lo que entra por teclado es de tipo texto 
#para hacer operaciones debes de convertirlo a tipo entero o decimal
sumamal=edad+num
print("'suma' de tu edad con el numero sin convertir a entero o decimal "+sumamal)

edadEntero=int(edad)#convierte a entero la variable edad
numdecimal=float(num)#convierte a decimal la variable num
sumabien=edadEntero+numdecimal
print("Suma de tu edad con el numero ya convertidos a entero y decimal: ",sumabien)

#manejo de if elif y else (sirven para hacer validaciones o comparaciones)
if edadEntero<=9: #si la edad es menor o igual a 9 entonces ejecuta lo siguiente
    print("cuerpo del if: ")
    print("Tienes menos de 9 o 9")
elif edadEntero>=10 and edadEntero<18: #si edad mayor o igual a 10 y edad menor a 18 (Se deben cumplir ambos) 
    print("Tienes entre 10 y 18") 
elif edadEntero==19 or edadEntero ==22:#si edad es 19 o edad es 22 (Solo se debe cumplir una de las 2)
    print("Tienes 19 o 22 años")
else:#si no se cumple ninguna de las anteriores
    print("tienes 18 o mas y no tienes 19 o 22")

if numdecimal!=5: #si numdecimal diferente de 5 entonces:
    print("ingresaste un numero diferente de 5")
else:
    print("ingresaste el 5")


#manejo de ciclos 

#FOR 
for i in range(10): 
    print(i) #imprime numeros desde 0 hasta numeros menores que 10 
             #una vez que llega a 10 se sale del ciclo 

print("for de 2 en 2: ")
for i in range(0,15,2):
    print(i)#imprime valores del 0 y menores que 15 de 2 en 2 

#while

n=1
print("Inicio while")
while n <=5: 
    print(n)#imprime numeros del 1 al 5
    n+=1
print("while terminado")

#while infinito

print("Inicio while infinito que termnina cuando ingresas un 3")
while True:
    j=input("ingresa un numero ")
    jint=int(j)
    if jint==3: #si ingresas un 3 entonces:
        break #break sirve para salir de un ciclo 
    #mientras no ingreses un 3 este ciclo no termina

#FUNCIONES

def imprimir_quetal(): #Asi se define una funcion
    print("que tal saludo desde mi funcion")

imprimir_quetal() #al hacer esto se ejecuta todo lo que contenga la funcion

#funcion con parametros:
def multiplicacion(ingreso):#funcion que le pasan un parametro 
    print(f"{ingreso} * 5 = {ingreso * 5}")

print("Funcion con parametro ")
multiplicacion(8)#a multiplicacion se le pasa el parametro 8 