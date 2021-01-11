cantidad= int(input("Ingrese la cantidad que tiene en el banco: "))
retiro=int(input("ingrese lo que va a retirar: "))
seguir="si"
while (seguir=="si"):
    while(retiro<cantidad):
        cantidad-=retiro
        print("la cantidad actual es: ",cantidad)
        if(retiro>=cantidad):
           print("NO HAY mas DINERO para RETIRAR")
    seguir=input("¿hará otro retiro?,indique si/no: ")    
    if seguir=="si":
        retiro=int(input("ingrese la cantidad que va a retirar: "))
    
    else:
            print("fin de la transaccion")  
    print("==========================================================")
