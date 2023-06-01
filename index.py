# Pedir 5 valores, sumarlos y mostrar el resultado.

valor1= Valor2 = Valor3= Valor4= Valor5= 0

valor1 = float(input("Ingrese el valor 1: "))
valor2 = float(input("Ingrese el valor 2: "))
valor3 = float(input("Ingrese el valor 3: "))
valor4 = float(input("Ingrese el valor 4: "))
valor5 = float(input("Ingrese el valor 5: "))

suma= valor1+valor2+valor3 + valor4 + valor5
print("La Suma de los valores es : ", suma) 


# Pedir desde que numero   hasta que numero va a mostrar

inicio= int(input("Ingrese el número desde el cual empezar: "))

mostrar= int(input("Ingrese el número hasta el cual mostrar: "))

for numero in range(inicio, mostrar+1):
    print(numero)
    


# Pedir 10 valores y contar cuantos numeros pares y cuantos impares ingresaron y mostrarlo en pantalla.

pares = 0 #-->Pongo las variables en cero para poder sumar
impares = 0

for i in range(10): #---> Aqui determino que ingrese 10 valores 
    
    valor = int(input("Ingrese el valor: ")) #-->utilizo un bucle "for" con "range(10)" para pedir que ingrese 10 valores
    
    if valor % 2 == 0: # En cada ingreso del valor, se lee si el valor es divisible por 2 es = 0 (es decir, es par)
        
        pares += 1   #--->entonces se incrementa "pares" 
    
    else:
        impares += 1 #--> sino es divisible en 2  , se incremente "impares"


print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
    


