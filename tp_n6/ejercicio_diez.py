matriz_cuacrada=[[2,5,6],[10,5,7],[8,1,4]]
matriz_diagonal=[]

for i in range(len(matriz_cuacrada)):
    for j in range(len(matriz_cuacrada)):
        if(i==j):
            matriz_diagonal.append(matriz_cuacrada[i][j])
            
print(matriz_diagonal)