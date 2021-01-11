#EJERCICIO 1: MOSTRAR LOS PRIMEROS 50 NÚMEROS

'''for i in range(1, 51):
 #   print(i)'''

#EJERCICIO 2: Hacer un algoritmo que guarde los numeros ingresados por el usuario, hasta que el usuario ingrese cero
#para que finalice el algoroitmo

'''num = int(input("Ingrese un número: "))

while num != 0 :
    num = int(input("Ingrese otro numero: ")) 

    if num == 0:
       print ("fin del programa")'''

#EJERCICIO 3: Hacer un algoritmo que muestre la tabla de multiplicar del número que ingrese el usuario.
#num = int(input("Ingrese un número: "))

'''if num != 0:
    i=0
    while i <= 12:
        result = num * i
        print('')
        print(num, '*', i, ' = ', result)
        i+=1'''


'''def tablaDeMultiplicar():
    if num != 0:
        i = 0
        while i <= 12:
            result = num * i
            print('')
            print(num, '*', i, ' = ', result)
            i += 1

tablaDeMultiplicar()'''

class Multiplicar:
        num = 0

        def tablaDeMultiplicar(self):
            self.setNumero()
            if self.getNumero() >= 0:
                i = 0
                while i <= 12:
                    result = self.num * i
                    print('')
                    print(self.num, '*', i, ' = ', result)
                    i += 1

        def setNumero(self):
            n = int(input("Ingrese un número: "))
            self.num = n
        def getNumero(self):
            return self.num
mult=Multiplicar()
mult.tablaDeMultiplicar()