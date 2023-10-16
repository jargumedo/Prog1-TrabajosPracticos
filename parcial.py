#Pide el nombre al usuario
name = input("Defina su nombre: ")
print(f"Hola {name}")
#Muestra el menu 
print("1) Juego de numeros")
print("2) Juego de palabras")
option=int(input(f"{name} elija un numero del menu: "))
#Declaro variables
higher_num=0
counter=0
counter_a=0
counter_e=0
counter_i=0
counter_o=0
counter_u=0
sumatory = 0


#Valido que el usuario elija una opcion valida para el menu
while(option!=1 and option!=2):
    print("Numero invalido, intentelo nuevamente")
    option=int(input(f"{name} elija 1 o 2: "))


#Se evalua la variable option y decide donde entrar
if(option==1):
    number=int(input(f"{name} elija un numero, coloque 0 si quiere salir: "))
    #Si el primer numero ingresado es par y es mayor que el numero almacenado en esa variable se reemplaza
    if(number%2==0 and number>higher_num):
            higher_num=number 
    #Condicion de salida
    while (number!=0):
        number=int(input(f"{name} elija un numero, coloque 0 si quiere salir: "))
        if(number%2==0 and number>higher_num):
            higher_num=number
        #Si el numero es impar se toma en cuenta para tomar el promedio
        elif(number%2==1):
             counter+=1
             sumatory=sumatory + number
    print(f"El promedio de los numeros impares es {round(sumatory/counter, 2)}")
    print(f"El numero par ingresado mas grande es {higher_num}")
elif(option==2):
    #Pide una frase para evaluar sus vocales
    phrase=input(f"{name} escriba una frase para ver cuantas vocales contiene: ")
    #recorre la frase para contar cada tipo de vocales
    for char in range(len(phrase)):
        if(phrase[char]=="a"):
            counter_a+=1
        elif(phrase[char]=="e"):
            counter_e+=1
        elif(phrase[char]=="i"):
            counter_i+=1
        elif(phrase[char]=="o"):
            counter_o+=1
        elif(phrase[char]=="u"):
            counter_u+=1
    
    print(f"{name} se utiliza {counter_a} veces a, {counter_e} veces e, {counter_i} veces i, {counter_o} veces o y {counter_u} veces u.")         


