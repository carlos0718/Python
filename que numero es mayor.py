print("=======ingrese tres numeros distintos========")
num1=int(input("ingrese primer numero: "))
num2=int(input("ingrese segundo numero: "))
num3=int(input("ingrese tercer numero: "))

if(num1>num2 and num1>num3):
  print ("el numero ", num1 , " es mayor")
elif (num2>num1 and num2>num3):
  print("el numero ", num2 , "es mayor")
else:
  print("el numero ", num3, " es mayor")
