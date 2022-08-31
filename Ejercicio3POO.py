class Persona:
    def __init__(self, nombre=None, edad=None, DNI=None):
        self.set_nombre(nombre)
        self.set_edad(edad)
        self.set_DNI(DNI)


    def set_nombre(self, nombre):
        if (nombre is None) or (isinstance(nombre, str)):
            self._nombre = nombre

        else:
            print("El valor del nombre no es valido")

    def set_edad(self, edad):
        if (edad is None) or (edad > 0) or (isinstance(edad, (int, float))):
            self._edad = edad

        else:
            print("El valor de la edad debe ser None o numerico (Int o Float) ")

    def set_DNI(self, DNI):
        if (DNI is None) or (isinstance(DNI, str)):
            self._DNI = DNI

        else:
            print("El valor del DNI no es valido")


    def get_nombre(self):
        return self._nombre

    def get_edad(self):
        return self._edad

    def get_DNI(self):
        return self._DNI


    
    def mostrar(self):
        print(f"Nombre: {self._nombre}, Edad: {self._edad}, DNI: {self._DNI}")

    def esMayorEdad(self):
        if (self._edad is not None) and (self._edad >= 18):
            return True

        else:
            return False





class Cuenta:
    def __init__(self, titular , cantidad=None):
        self.set_titular(titular)
        self.set_cantidad(cantidad)


    def set_titular(self, titular):
        if (not isinstance(titular, Persona)):
            print("El titular es invalido. Debe ser un objeto de la clase Persona")

        else:
            self._titular = titular


    def set_cantidad(self, cantidad):
        if (cantidad > 0) or (cantidad is None) or (isinstance(cantidad, (int, float))):
            self._cantidad = cantidad

        else:
            print("El valor de la cantidad debe ser None o numerico (Int o Float) ")


    def get_titular(self):
        return self._titular

    
    def get_cantidad(self):
        return self._cantidad


    def mostrar(self):
        print(f"""
        Titular
            Nombre: {self._titular.get_nombre()}, Edad: {self._titular.get_edad()}, DNI: {self._titular.get_DNI()}

        Cantidad actual
            {self._cantidad}    
        """)


    def ingresar(self, cantidad):
        if (isinstance(cantidad, (int, float))) and (cantidad >= 0):
            self._cantidad += cantidad


    def retirar(self, cantidad):
        if (isinstance(cantidad, (int, float))):
            self._cantidad -= cantidad





class CuentaJoven (Cuenta):
    def __init__(self, titular,bonificacion, cantidad=None):
        Cuenta.__init__(self, titular, cantidad)
        self.set_bonificacion(bonificacion)


    def set_bonificacion(self, bonificacion):
        if (isinstance(bonificacion, (int, float))) and (bonificacion > 0):
            self._bonificacion = bonificacion

        else:
            print("La bonificación debe ser positiva")


    def get_bonificacion(self):
        return self._bonificacion

    
    def esTitularValido(self):
        titular = self.get_titular()
        edad = titular.get_edad()

        if edad >= 18 and edad < 25:
            return True

        else:
            return False


    def retirar(self, cantidad):
        if self.esTitularValido() == True and (isinstance(cantidad, (int, float))):
            self._cantidad -= cantidad


    def mostrar(self):
        print(f"Cuenta Joven. Bonificación: {self._bonificacion}")

    




# Testeando clases

print("------------------------------------------------------------------")
persona_sin_datos = Persona()
persona_sin_datos.mostrar()
print("Es mayor de edad: ", persona_sin_datos.esMayorEdad())

persona_con_datos = Persona(nombre="Maria", edad=50, DNI="123456")
persona_con_datos.mostrar()
print("Es mayor de edad: ", persona_con_datos.esMayorEdad())

persona_con_datos.set_DNI("7894")
persona_con_datos.set_edad(True)

print("------------------------------------------------------------------")

cuenta_1 = Cuenta(titular=persona_con_datos, cantidad=100)
cuenta_1.ingresar("54AAAx")
cuenta_1.ingresar(5000)
cuenta_1.retirar(600)
print(cuenta_1.get_cantidad())
cuenta_1.mostrar()


print("------------------------------------------------------------------")

cuenta_joven_1 = CuentaJoven(titular=persona_con_datos, cantidad=9000, bonificacion=60)
print("El titular es valido: ", cuenta_joven_1.esTitularValido())
cuenta_joven_1.retirar(400)
print(cuenta_joven_1.get_bonificacion())
