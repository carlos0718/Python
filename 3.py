import ej2 

num1=int(input("ingrese primer numero: "))
num2=int(input("ingrese segundo numero: "))
num3=int(input("ingrese tercer numero: "))
num4=int(input("ingrese cuarto numero: "))

cont =0
'''for i in range(0,5):'''
if(num1%3==0):
    cont=+1
if(num2%3==0):
    cont=+1
if(num3%3==0):
    cont=+1
if(num4%3==0):
    cont=+1    
print("los multiplos de 3 son: "+ cont)        
