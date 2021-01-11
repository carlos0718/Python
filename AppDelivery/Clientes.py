import os
import io

ARCHIVO_CLIENTES = " CLIENTES.txt"
class Clientes():
    nombre = " "
    apellido =" "
    mail =" "
    domicilio =" "

    def setNombre(self):
        nom = input("Nombre: ")
        while nom == '\0':
            nom = input("Nombre: ")
        self.nombre=nom
    def getNombre(self):
        return self.nombre
    def setApellido(self):
        ape = input("Apellido: ")
        while ape == '\0':
            ape = input("Nombre: ")
        self.apellido = ape
    def getApellido(self):
        return self.apellido
    def setMail(self):
        m = input("Mail: ")
        while m == '\0':
            m = input("Mail: ")
        self.mail=m
    def getMail(self):
        return self.mail
    def setDomicilio(self):
        dom = input("Nombre: ")
        while dom == '\0':
            dom = input("Nombre: ")
        self.domicilio=dom
    def getDomicilio(self):
        return self.domicilio

    def cargarClientes(self):
        
        self.setNombre()
        self.setApellido()
        self.setMail()

    def mostrarClientes(self):
        os.system("cls")
        print("Nombre\t Apellido\t Mail")
        print("________________________________")
        print(self.getNombre(),"\t", self.getApellido(),"\t",self.getMail())

    def guardarEnDisco(self):
        archivo=open(ARCHIVO_CLIENTES,"a")
        archivo.write(self.cargarClientes())
        archivo.close()

    def leerDeDisco(self):
        archivo=open(ARCHIVO_CLIENTES,"r")
        archivo.read(self.mostrarClientes())
        archivo.close()






