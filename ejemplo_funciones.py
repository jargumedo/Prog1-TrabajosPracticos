from funciones import *
number=int(input("Defina un numero: "))
digits_sumatory=0
numbers_sumatory=0

while number!=0:
    print(f"Suma: {sumDigits(number)}")
    digits_sumatory+=sumDigits(number)
    numbers_sumatory+=number
    number=int(input("Defina un numero: "))
    

print(f"La suma de los numeros ingresados es: {numbers_sumatory}")
print(f"La suma de los digitos de la sumatoria de los numeros ingresados es: {sumDigits(numbers_sumatory)}")