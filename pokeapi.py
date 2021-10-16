#PARA EJECUTAR ESTE PROGRAMA REVISA PRIMERO EL DOCUMENTO DE COMO INSTALAR LIBRERIAS 
#link pokeapi
# https://pokeapi.co

import requests #libreria para hacer peticiones HTTP
#librerias para usar graficas
import matplotlib.pyplot as plt #plt para mostrar imagenes
import matplotlib.image as img #img para leer la imagen

pokemon=input("Ingresa el nombre de un pokemon ")
url="https://pokeapi.co/api/v2/pokemon/"+pokemon #url de la imagen del pokemon 
res = requests.get(url)#hace solicitud a la pagina y regresa el codigo de status

if res.status_code ==200: #si el status es 200 la peticion fue correcta 
    fotopokemon=img.imread(res.json()['sprites']['front_default'])#carga la imagen desde el archivo de sprites/front_default
    plt.title(res.json()['name'])#se le pone de titulo el nombre del pokemon que ingresamos y que esta en name
    plotearimagen=plt.imshow(fotopokemon)#muestra la imagen en el recuadro de la grafica
    plt.show()#nos muestra la grafica en este caso la imagen del pokemon que ingresamos
else: #si el estatus no es correcto entonces:
    print("pokemon no encontrado :0")#nos informa que no encontro el pokemon
    exit() #sale del programa