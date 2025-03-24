class Persona():
    def __init__(self, nombre, cedula, genero):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__genero = genero

    def verNombre(self): 
        return self.__nombre

    def verCedula(self):
        return self.__cedula

    def verGenero(self):
        return self.__genero


class Paciente(Persona):
    def __init__(self, nombre, cedula, genero, servicio):
        super().__init__(nombre, cedula, genero)
        self.__servicio = servicio

    def verServicio(self):
        return self.__servicio


class Sistema:
    def __init__(self):
        self.lista_pacientes = {}

    def agregar_paciente(self, paciente):
        """Verifica si ya existe un paciente con la misma cédula antes de agregarlo."""
        if paciente.verCedula() in self.lista_pacientes:
            print("Error: Ya existe un paciente con esta cédula.")
            return False
        else:
            self.lista_pacientes[paciente.verCedula()] = paciente
            print("Paciente registrado exitosamente.")
            return True

    def obtener_paciente(self, cedula):
        """Devuelve el paciente si existe, de lo contrario None."""
        return self.lista_pacientes.get(cedula, None)

    def contar_pacientes(self):
        """Devuelve el número de pacientes en el sistema."""
        return len(self.lista_pacientes)


def main():
    sistema = Sistema()

    while True:
        print("\nMenú del Sistema de Pacientes")
        print("1. Ingresar un paciente nuevo")
        print("2. Ver todos los datos de un paciente existente")
        print("3. Ver número de pacientes en el sistema")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del paciente: ")
            cedula = input("Ingrese la cédula del paciente: ")
            
            # Verificar si la cédula ya está registrada
            if sistema.obtener_paciente(cedula):
                print("Error: Ya existe un paciente con esta cédula.")
                continue

            genero = input("Ingrese el género del paciente: ")
            servicio = input("Ingrese el servicio asignado: ")

            paciente = Paciente(nombre, cedula, genero, servicio)
            sistema.agregar_paciente(paciente)

        elif opcion == "2":
            cedula = input("Ingrese la cédula del paciente a buscar: ")
            paciente = sistema.obtener_paciente(cedula)

            if paciente:
                print("\nDatos del paciente:")
                print(f"Nombre: {paciente.verNombre()}")
                print(f"Cédula: {paciente.verCedula()}")
                print(f"Género: {paciente.verGenero()}")
                print(f"Servicio: {paciente.verServicio()}")
            else:
                print("Paciente no encontrado.")

        elif opcion == "3":
            print(f"Número de pacientes registrados: {sistema.contar_pacientes()}")

        elif opcion == "4":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
