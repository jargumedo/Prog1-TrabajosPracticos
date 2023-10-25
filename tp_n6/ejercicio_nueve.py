memotest=[[1,2,3,4,5],[2,3,4,5,1]]
coincidencias=[]
# print("Vamos a jugar al memotest, debe elegir dos numeros para ver si su carta es igual que la proxima")
for i in memotest:
    print(" ")
    for j in i:
        print("_", end=" ")
        
print(" ")
        
numero11=int(input("Defina el numero 1 de la primer carta: "))
numero12=int(input("Defina el numero 2 de la primer carta: "))
#print(memotest[numero11][numero12])

for i in range(len(memotest)):
    print(" ")
    for j in range(len(memotest[i])):
        if(numero12==j and numero11==i):
            print(memotest[numero11][numero12], end=" ")
        else:
            print("_", end=" ")
            
print(" ")
            
numero21=int(input("Defina el numero 1 de la segunda carta: "))
numero22=int(input("Defina el numero 2 de la segunda carta: "))

for i in range(len(memotest)):
    print(" ")
    for j in range(len(memotest[i])):
        if(numero22==j and numero21==i):
            print(memotest[numero21][numero22], end=" ")
        else:
            print("_", end=" ")

print(" ")
            
if(memotest[numero11][numero12]==memotest[numero21][numero22]):
    coincidencias.append(memotest[numero11][numero12])
    for i in range(len(memotest)):
        print(" ")
        for j in range(len(memotest[i])):
            if(memotest[i][j] in coincidencias):
                print(memotest[i][j], end=" ")
            else:
                print("_", end=" ")

print(" ")

while (len(coincidencias)<5):
    numero11=int(input("Defina el numero 1 de la primer carta: "))
    numero12=int(input("Defina el numero 2 de la primer carta: "))
    #print(memotest[numero11][numero12])

    for i in range(len(memotest)):
        print(" ")
        for j in range(len(memotest[i])):
            if(numero12==j and numero11==i):
                print(memotest[numero11][numero12], end=" ")
            else:
                print("_", end=" ")
                
    print(" ")
                
    numero21=int(input("Defina el numero 1 de la segunda carta: "))
    numero22=int(input("Defina el numero 2 de la segunda carta: "))

    for i in range(len(memotest)):
        print(" ")
        for j in range(len(memotest[i])):
            if(numero22==j and numero21==i):
                print(memotest[numero21][numero22], end=" ")
            else:
                print("_", end=" ")

    print(" ")
                
    if(memotest[numero11][numero12]==memotest[numero21][numero22]):
        coincidencias.append(memotest[numero11][numero12])
        for i in range(len(memotest)):
            print(" ")
            for j in range(len(memotest[i])):
                if(memotest[i][j] in coincidencias):
                    print(memotest[i][j], end=" ")
                else:
                    print("_", end=" ")
    
print("Felicidades, ganaste!!!")



