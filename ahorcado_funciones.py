import random
from funciones import *


#Declaro las palabras
list_ahorcado = ["pelota","tomate", "futbol", "amarillo", "beisbol", "bicicleta", "tenis", "jarra", "cuchara", "tenedor"]
letras_usadas=[]

#Asigna y convierte a lista

palabra_seleccionada=random.choice(list_ahorcado)
palabra = rellena_guiones(palabra_seleccionada)

#Establecemos las vidas
lives_left=6


#Rellenar palabra
palabra = list(palabra)
print(palabra)
contador =0 

#Mientras tenga vidas y no haya completado la palabra entra al bucle

while(lives_left>0 and contador < len(palabra_seleccionada)):
    #Pedir al usuario la palabra
    letra_seleccionada= ingresa_letra()
    
    #La letra tiene que estar en la palabra
    if(letra_seleccionada in palabra_seleccionada):
        #Si la letra ingresada no se repite con una ya ingresada anteriormente entra
        if(letra_seleccionada not in palabra):
            print("Correcto")
            for i in range (len(palabra_seleccionada)):
                if (letra_seleccionada == palabra_seleccionada[i]):
                    palabra[i] = letra_seleccionada
                    print(palabra)
                    contador+=1
                    continue
            letras_usadas.append(letra_seleccionada)
            print(f"Letras ingresadas: {letras_usadas}")
        else:
            print("La letra ya fue ingresada")
            print(f"Letras ingresadas: {letras_usadas}")
            print(lives_left)
        
    else:
        if(letra_seleccionada in letras_usadas):
            print("La letra ya fue ingresada")
        else:
            print("Letra incorrecta")
            print(palabra)
            letras_usadas.append(letra_seleccionada)
            lives_left=lives_left-1
            print(f"Vidas restantes {lives_left}")
            print(f"Letras ingresadas: {letras_usadas}")
    
    
#Si queda sin vidas muestra un mensaje de derrota, si no de victoria
resultado_ahorcado(lives_left, palabra_seleccionada)