def sumDigits(number):
    add=0
    while number!=0:
        resto=number%10
        number//=10
        add+=resto
        
    return add
        
def rellena_guiones(word):
    word=list(word)
    for x in range(len(word)):
        word[x]="_"
        
    return (word)

def ingresa_letra():
    
    letra=input("Ingrese una letra para buscar: ").lower()
    while len(letra)!=1:
        print("Debe ingresar una sola letra, intente de nuevo")
        letra=input("Ingrese una letra para buscar: ").lower()
    
    return letra
    
def resultado_ahorcado(vidas, palabra):
    if(vidas == 0):
        print(f"Perdiste, la palabra era {palabra}")
    else:
        print("Felicidades, ganaste maquina")

def is_power(n, b) -> bool:
    if n == 1:
        return True
    elif n % b != 0 or n == 0:
        return False
    else:
        return is_power(n / b, b)
    
