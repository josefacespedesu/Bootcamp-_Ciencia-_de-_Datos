<<<<<<< HEAD
# =========================
# FUNCIONES DE VALIDACIÓN
# =========================

# Verifica que el nombre contenga solo letras y espacios. Usa isalpha() para asegurar que no haya números ni símbolos.
def validar_nombre(nombre):
    return nombre.replace(" ", "").isalpha()

#Comprueba que el teléfono esté compuesto únicamente por números. Evita el ingreso de letras u otros caracteres.
def validar_telefono(telefono):
    return telefono.isdigit()

# Realiza una validación básica del correo electrónico. Verifica que contenga los caracteres @ y "."
def validar_correo(correo):
    return "@" in correo and "." in correo

# Solicita el nombre al usuario. Utiliza un while para repetir la solicitud hasta que el dato sea válido.
def pedir_nombre():
    while True:
        nombre = input("Nombre: ")
        if validar_nombre(nombre):
            return nombre
        else:
            print("\n❌ EL NOMBRE SOLO DEBE CONTENER LETRAS.")
#Solicita el número de teléfono. Utiliza un while, garantizando que el dato ingresado sea numérico antes de continuar.
def pedir_telefono():
    while True:
        telefono = input("Teléfono: ")
        if validar_telefono(telefono):
            return telefono
        else:
            print("\n❌ EL TELÉFONO SOLO DEBE CONTENER NÚMEROS.")
#Solicita el correo electrónico. Repite la solicitud mientras el formato del correo sea incorrecto.
def pedir_correo():
    while True:
        correo = input("Correo: ")
        if validar_correo(correo):
            return correo
        else:
            print("\n❌ CORREO INVÁLIDO. DEBE CONTENER '@' Y '.'")


# =========================
# CLASE CONTACTO
# =========================
# Constructor de la clase. Inicializa un diccionario llamado datos donde se almacena toda la información del contacto. Nombre, teléfono, corre y dirección
class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        # Diccionario que almacena los datos del contacto
        self.datos = {
            "nombre": nombre,
            "telefono": telefono,
            "correo": correo,
            "direccion": direccion
        }
# Muestra en pantalla los datos del contacto de forma ordenada. Facilita la visualización de la información.
    def mostrar(self):
        """Muestra la información del contacto"""
        print("-" * 35)
        print(f"Nombre: {self.datos['nombre']}")
        print(f"Teléfono: {self.datos['telefono']}")
        print(f"Correo: {self.datos['correo']}")
        print(f"Dirección: {self.datos['direccion']}")
        print("-" * 35)
#Permite modificar los datos del contacto. Actualiza los valores dentro del diccionario.
    def actualizar_datos(self, nombre, telefono, correo, direccion):
        """Actualiza los datos del contacto"""
        self.datos["nombre"] = nombre
        self.datos["telefono"] = telefono
        self.datos["correo"] = correo
        self.datos["direccion"] = direccion


# =========================
# CLASE AGENDA DE CONTACTOS
# =========================
#Clase agenda de contactos 
class AgendaContactos:
    def __init__(self): 
        # Inicializa una lista vacía que almacenará todos los contactos.
        self.contactos = []

    def agregar_contacto(self, contacto):
        #Agrega un objeto Contacto a la lista. Permite registrar nuevos contactos.
        self.contactos.append(contacto)
        print("\n✅ CONTACTO AGREGADO CORRECTAMENTE.")

    def buscar_contacto(self, dato):
        # Recorre la lista de contactos. Permite buscar un contacto por nombre o teléfono.
        for contacto in self.contactos:
            if (contacto.datos["nombre"].lower() == dato.lower() or
                contacto.datos["telefono"] == dato):
                return contacto
        return None

    def editar_contacto(self, dato):
        #Busca el contacto y permite actualizar su información. Asimismo utiliza las funciones de validación para los nuevos datos.
        contacto = self.buscar_contacto(dato)
        if contacto:
            print("Ingrese los nuevos datos:")
            nombre= pedir_nombre ()
            telefono = pedir_telefono()
            correo = pedir_correo()
            direccion = input("Dirección: ")
            contacto.actualizar_datos(nombre,telefono, correo, direccion)
            print("\n✅ CONTACTO ACTUALIZADO.")
        else:
            print("\n❌ CONTACTO NO ENCONTRADO.")

    def eliminar_contacto(self, dato):
        # Busca y elimina un contacto de la lista.
        contacto = self.buscar_contacto(dato)
        if contacto:
            self.contactos.remove(contacto)
            print("\n✅ CONTACTO ELIMINADO.")
        else:
            print("\n❌ CONTACTO NO ENCONTRADO.")

    def mostrar_contactos(self):
        # Muestra todos los contactos registrados. Verifica previamente si la lista está vacía.
        if not self.contactos:
            print("\n📂 NO HAY CONTACTOS REGISTRADOS.")
        else:
            for contacto in self.contactos:
                contacto.mostrar()


# =========================
# PROGRAMA PRINCIPAL (MENÚ)
# =========================
def menu():
    #Muestra la interfaz principal del sistema. Permite al usuario interactuar con la aplicación mediante opciones numéricas. Controla el flujo del programa usando un while.
    #Representa la interfaz de usuario en consola.
    agenda = AgendaContactos()

    while True:
    # Crea un bucle infinito.
    # Como True siempre es verdadero, el menú se vuelve a mostrar una y otra vez, permitiendo que el usuario realice varias acciones sin que el programa termine.

        print("\n===================================")
        print("   SISTEMA DE GESTIÓN DE CONTACTOS  ")
        print("===================================")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = pedir_nombre()
            telefono = pedir_telefono()
            correo = pedir_correo()
            direccion = input("Dirección: ")
            nuevo_contacto = Contacto(nombre, telefono, correo, direccion)
            agenda.agregar_contacto(nuevo_contacto)

        elif opcion == "2":
            dato = input("Ingrese nombre o teléfono: ")
            contacto = agenda.buscar_contacto(dato)
            if contacto:
                contacto.mostrar()
            else:
                print("\n❌ CONTACTO NO ENCONTRADO.")

        elif opcion == "3":
            dato = input("Ingrese nombre o teléfono del contacto a editar: ")
            agenda.editar_contacto(dato)

        elif opcion == "4":
            dato = input("Ingrese nombre o teléfono del contacto a eliminar: ")
            agenda.eliminar_contacto(dato)

        elif opcion == "5":
            agenda.mostrar_contactos()

        elif opcion == "6":
            #El ciclo solo se detiene cuando el usuario elige la opción “Salir”, momento en el cual se ejecuta la instrucción break, que finaliza el while.
            print("\n👋 SALIENDO DEL SISTEMA...")
            break

        else:
            print("\n❌ OPCIÓN INVÁLIDA.")


# =========================
# EJECUCIÓN DEL PROGRAMA
# =========================
=======
# =========================
# FUNCIONES DE VALIDACIÓN
# =========================

# Verifica que el nombre contenga solo letras y espacios. Usa isalpha() para asegurar que no haya números ni símbolos.
def validar_nombre(nombre):
    return nombre.replace(" ", "").isalpha()

#Comprueba que el teléfono esté compuesto únicamente por números. Evita el ingreso de letras u otros caracteres.
def validar_telefono(telefono):
    return telefono.isdigit()

# Realiza una validación básica del correo electrónico. Verifica que contenga los caracteres @ y "."
def validar_correo(correo):
    return "@" in correo and "." in correo

# Solicita el nombre al usuario. Utiliza un while para repetir la solicitud hasta que el dato sea válido.
def pedir_nombre():
    while True:
        nombre = input("Nombre: ")
        if validar_nombre(nombre):
            return nombre
        else:
            print("\n❌ EL NOMBRE SOLO DEBE CONTENER LETRAS.")
#Solicita el número de teléfono. Utiliza un while, garantizando que el dato ingresado sea numérico antes de continuar.
def pedir_telefono():
    while True:
        telefono = input("Teléfono: ")
        if validar_telefono(telefono):
            return telefono
        else:
            print("\n❌ EL TELÉFONO SOLO DEBE CONTENER NÚMEROS.")
#Solicita el correo electrónico. Repite la solicitud mientras el formato del correo sea incorrecto.
def pedir_correo():
    while True:
        correo = input("Correo: ")
        if validar_correo(correo):
            return correo
        else:
            print("\n❌ CORREO INVÁLIDO. DEBE CONTENER '@' Y '.'")


# =========================
# CLASE CONTACTO
# =========================
# Constructor de la clase. Inicializa un diccionario llamado datos donde se almacena toda la información del contacto. Nombre, teléfono, corre y dirección
class Contacto:
    def __init__(self, nombre, telefono, correo, direccion):
        # Diccionario que almacena los datos del contacto
        self.datos = {
            "nombre": nombre,
            "telefono": telefono,
            "correo": correo,
            "direccion": direccion
        }
# Muestra en pantalla los datos del contacto de forma ordenada. Facilita la visualización de la información.
    def mostrar(self):
        """Muestra la información del contacto"""
        print("-" * 35)
        print(f"Nombre: {self.datos['nombre']}")
        print(f"Teléfono: {self.datos['telefono']}")
        print(f"Correo: {self.datos['correo']}")
        print(f"Dirección: {self.datos['direccion']}")
        print("-" * 35)
#Permite modificar los datos del contacto. Actualiza los valores dentro del diccionario.
    def actualizar_datos(self, nombre, telefono, correo, direccion):
        """Actualiza los datos del contacto"""
        self.datos["nombre"] = nombre
        self.datos["telefono"] = telefono
        self.datos["correo"] = correo
        self.datos["direccion"] = direccion


# =========================
# CLASE AGENDA DE CONTACTOS
# =========================
#Clase agenda de contactos 
class AgendaContactos:
    def __init__(self): 
        # Inicializa una lista vacía que almacenará todos los contactos.
        self.contactos = []

    def agregar_contacto(self, contacto):
        #Agrega un objeto Contacto a la lista. Permite registrar nuevos contactos.
        self.contactos.append(contacto)
        print("\n✅ CONTACTO AGREGADO CORRECTAMENTE.")

    def buscar_contacto(self, dato):
        # Recorre la lista de contactos. Permite buscar un contacto por nombre o teléfono.
        for contacto in self.contactos:
            if (contacto.datos["nombre"].lower() == dato.lower() or
                contacto.datos["telefono"] == dato):
                return contacto
        return None

    def editar_contacto(self, dato):
        #Busca el contacto y permite actualizar su información. Asimismo utiliza las funciones de validación para los nuevos datos.
        contacto = self.buscar_contacto(dato)
        if contacto:
            print("Ingrese los nuevos datos:")
            nombre= pedir_nombre ()
            telefono = pedir_telefono()
            correo = pedir_correo()
            direccion = input("Dirección: ")
            contacto.actualizar_datos(nombre,telefono, correo, direccion)
            print("\n✅ CONTACTO ACTUALIZADO.")
        else:
            print("\n❌ CONTACTO NO ENCONTRADO.")

    def eliminar_contacto(self, dato):
        # Busca y elimina un contacto de la lista.
        contacto = self.buscar_contacto(dato)
        if contacto:
            self.contactos.remove(contacto)
            print("\n✅ CONTACTO ELIMINADO.")
        else:
            print("\n❌ CONTACTO NO ENCONTRADO.")

    def mostrar_contactos(self):
        # Muestra todos los contactos registrados. Verifica previamente si la lista está vacía.
        if not self.contactos:
            print("\n📂 NO HAY CONTACTOS REGISTRADOS.")
        else:
            for contacto in self.contactos:
                contacto.mostrar()


# =========================
# PROGRAMA PRINCIPAL (MENÚ)
# =========================
def menu():
    #Muestra la interfaz principal del sistema. Permite al usuario interactuar con la aplicación mediante opciones numéricas. Controla el flujo del programa usando un while.
    #Representa la interfaz de usuario en consola.
    agenda = AgendaContactos()

    while True:
    # Crea un bucle infinito.
    # Como True siempre es verdadero, el menú se vuelve a mostrar una y otra vez, permitiendo que el usuario realice varias acciones sin que el programa termine.

        print("\n===================================")
        print("   SISTEMA DE GESTIÓN DE CONTACTOS  ")
        print("===================================")
        print("1. Agregar contacto")
        print("2. Buscar contacto")
        print("3. Editar contacto")
        print("4. Eliminar contacto")
        print("5. Mostrar todos los contactos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = pedir_nombre()
            telefono = pedir_telefono()
            correo = pedir_correo()
            direccion = input("Dirección: ")
            nuevo_contacto = Contacto(nombre, telefono, correo, direccion)
            agenda.agregar_contacto(nuevo_contacto)

        elif opcion == "2":
            dato = input("Ingrese nombre o teléfono: ")
            contacto = agenda.buscar_contacto(dato)
            if contacto:
                contacto.mostrar()
            else:
                print("\n❌ CONTACTO NO ENCONTRADO.")

        elif opcion == "3":
            dato = input("Ingrese nombre o teléfono del contacto a editar: ")
            agenda.editar_contacto(dato)

        elif opcion == "4":
            dato = input("Ingrese nombre o teléfono del contacto a eliminar: ")
            agenda.eliminar_contacto(dato)

        elif opcion == "5":
            agenda.mostrar_contactos()

        elif opcion == "6":
            #El ciclo solo se detiene cuando el usuario elige la opción “Salir”, momento en el cual se ejecuta la instrucción break, que finaliza el while.
            print("\n👋 SALIENDO DEL SISTEMA...")
            break

        else:
            print("\n❌ OPCIÓN INVÁLIDA.")


# =========================
# EJECUCIÓN DEL PROGRAMA
# =========================
>>>>>>> f4cecb7a8e66d9544b6e6f1774552278f8131a93
menu()