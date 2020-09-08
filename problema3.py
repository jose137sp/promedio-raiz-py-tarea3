def promedio(nota1,nota2,nota3,nota4,nota5,parcial,final):
    nf=nota1+nota2+nota3+nota4+nota5
    pprac= (nf/5) #promedio de las 5 practicas
    pprac2= (pprac*35)/100 #promedio a 35% de las practicas

    pparcial=(parcial*32.5)/100 #25% parcial
    psemestral=(final*32.5)/100 #50% semestral

    promediofinal= (pprac2+pparcial+psemestral) #promediofinal

    return(promediofinal)

x=True
while x:
        try:
            nota1=(float(input("\nIntroduzca la nota de la practica 1: ")))
            nota2=(float(input("Introduzca la nota de la practica 2: ")))
            nota3=(float(input("Introduzca la nota de la practica 3: ")))
            nota4=(float(input("Introduzca la nota de la practica 4: ")))
            nota5=(float(input("Introduzca la nota de la practica 5: ")))
            parcial=(float(input("Introduzca la nota del parcial: ")))
            final=(float(input("Introduzca la nota del semestral: ")))
            x=False
        except ValueError:
            print("\nIntrodujo un valor incorrecto, vuelva a introducir TODAS las calificaciones nuevamente.")


print("\nSu promedio final es: ", promedio(nota1,nota2,nota3,nota4,nota5,parcial,final)+("\n"))