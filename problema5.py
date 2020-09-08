import math

def raiz_cubica(a):
    raiz3=(a)**(1/3) 
    return(raiz3)

def raiz_cuadrada(a):
    raiz2=math.sqrt(a)
    return(raiz2)

x=True
while x:
        try:
            dato=(int(input("\nIntroduzca un dato de tipo entero para calcular su raiz cuadrada y raiz cubica: ")))
            x=False
        except ValueError:
            print("No introdujo un numero entero")
            
print("La raiz cuadrada es: ", raiz_cuadrada(dato))
print("La raiz cubica es: ", raiz_cubica(dato))





    

