#Un trabajador necesita calcular su salario semanal, el cual se obtiene de la siguiente manera
#si trabaja 40hs o menos se le paga un salario de $16 pesos por hora. Si trabaja mas de 40hs,
#cada hora extra se le paga $20 pesos la hora extra. El usuario debe ingresar la cantidad de
#de horas trabajadas para saber su salario final.

trabajoHoras = int(input("INGRESE LA CANTIDAD DE HORAS TRABAJADAS:  "))
if trabajoHoras <= 40:
    salario = trabajoHoras * 16
if trabajoHoras > 40:
    salario = trabajoHoras * 20

print("SALARIO TOTAL: ", salario)
