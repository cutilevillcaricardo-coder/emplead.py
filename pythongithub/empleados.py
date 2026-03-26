# empleados.py - Sistema de Empleados con Herencia y Polimorfismo

class Empleado:
    """Clase base que representa a cualquier empleado"""

    def __init__(self, nombre, edad, salario_base, anos_experiencia=0):
        # Atributos públicos
        self.nombre = nombre
        self.edad = edad
        self.anos_experiencia = anos_experiencia
        # Atributo protegido (convención: _ significa "no tocar directamente")
        self._salario_base = salario_base

    def calcular_salario(self):
        """Metodo base que será sobrescrito por las clases hijas"""
        return self._salario_base

    def mostrar_info(self):
        """Muestra la información básica del empleado"""
        return (f"Empleado: {self.nombre}, Edad: {self.edad}, "
                f"Años exp: {self.anos_experiencia}, "
                f"Salario: ${self.calcular_salario():.2f}")

    def aumentar_salario(self, porcentaje):
        """Aumenta el salario base del empleado según un porcentaje"""
        incremento = self._salario_base * (porcentaje / 100)
        self._salario_base += incremento
        return self._salario_base


class Gerente(Empleado):
    """Gerente - Hereda de Empleado"""

    def __init__(self, nombre, edad, salario_base, bono, departamento, anos_experiencia=0):
        # Llamar al constructor de la clase padre
        super().__init__(nombre, edad, salario_base, anos_experiencia)

        # Atributos específicos de Gerente
        self.bono = bono
        self.departamento = departamento

    def calcular_salario(self):
        """SOBRESCRITURA: El salario del gerente incluye el bono"""
        return self._salario_base + self.bono

    def mostrar_info(self):
        """SOBRESCRITURA: Mostrar información específica del gerente"""
        return (f"Gerente: {self.nombre}, Edad: {self.edad}, "
                f"Años exp: {self.anos_experiencia}, "
                f"Departamento: {self.departamento}, "
                f"Salario: ${self.calcular_salario():.2f} "
                f"(Base: ${self._salario_base:.2f} + Bono: ${self.bono:.2f})")


class Desarrollador(Empleado):
    """Desarrollador - Hereda de Empleado"""

    def __init__(self, nombre, edad, salario_base, lenguaje, horas_extra=0, pago_hora=50, anos_experiencia=0):
        super().__init__(nombre, edad, salario_base, anos_experiencia)

        # Atributos específicos
        self.lenguaje = lenguaje
        self.horas_extra = horas_extra
        self.pago_hora = pago_hora

    def calcular_salario(self):
        """SOBRESCRITURA: El desarrollador gana extra por horas extra"""
        extra = self.horas_extra * self.pago_hora
        return self._salario_base + extra

    def mostrar_info(self):
        """SOBRESCRITURA: Mostrar información específica"""
        extra = self.horas_extra * self.pago_hora
        return (f"Desarrollador: {self.nombre}, Edad: {self.edad}, "
                f"Años exp: {self.anos_experiencia}, "
                f"Lenguaje: {self.lenguaje}, "
                f"Salario: ${self.calcular_salario():.2f} "
                f"(Base: ${self._salario_base:.2f} + "
                f"HE: {self.horas_extra} x ${self.pago_hora:.2f} = ${extra:.2f})")


class Practicante(Empleado):
    """Practicante - Hereda de Empleado y gana el 70% del salario base"""

    def __init__(self, nombre, edad, salario_base, universidad, anos_experiencia=0):
        super().__init__(nombre, edad, salario_base, anos_experiencia)
        self.universidad = universidad

    def calcular_salario(self):
        """SOBRESCRITURA: El practicante gana el 70% del salario base"""
        return self._salario_base * 0.70

    def mostrar_info(self):
        """SOBRESCRITURA: Mostrar información específica del practicante"""
        return (f"Practicante: {self.nombre}, Edad: {self.edad}, "
                f"Años exp: {self.anos_experiencia}, "
                f"Universidad: {self.universidad}, "
                f"Salario: ${self.calcular_salario():.2f} "
                f"(70% de Base: ${self._salario_base:.2f})")


def mostrar_nomina(empleados):
    """FUNCION QUE DEMUESTRA POLIMORFISMO"""
    print("\n" + "=" * 60)
    print("NOMINA DE EMPLEADOS")
    print("=" * 60)

    total_nomina = 0

    for empleado in empleados:
        # POLIMORFISMO: Aunque todos son tipos diferentes,
        # todos entienden los mismos métodos
        print(empleado.mostrar_info())
        total_nomina += empleado.calcular_salario()

    print("=" * 60)
    print(f"TOTAL NOMINA: ${total_nomina:.2f}")
    print("=" * 60)


def mostrar_menu():
    """Muestra las opciones disponibles"""
    print("\n" + "=" * 50)
    print("SISTEMA DE GESTIÓN DE EMPLEADOS")
    print("=" * 50)
    print("1. Agregar empleado regular")
    print("2. Agregar gerente")
    print("3. Agregar desarrollador")
    print("4. Agregar practicante")
    print("5. Ver todos los empleados")
    print("6. Calcular salario de un empleado")
    print("7. Aumentar salario a un empleado")
    print("8. Ver total de nómina")
    print("9. Salir")
    print("-" * 50)


def agregar_empleado(empleados):
    """Agrega un empleado regular"""
    print("\n--- NUEVO EMPLEADO REGULAR ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    anos_exp = int(input("Años de experiencia: "))

    nuevo = Empleado(nombre, edad, salario, anos_exp)
    empleados.append(nuevo)
    print(f"✓ Empleado {nombre} agregado exitosamente")
    return empleados


def agregar_gerente(empleados):
    """Agrega un gerente"""
    print("\n--- NUEVO GERENTE ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    bono = float(input("Bono: $"))
    depto = input("Departamento: ")
    anos_exp = int(input("Años de experiencia: "))

    nuevo = Gerente(nombre, edad, salario, bono, depto, anos_exp)
    empleados.append(nuevo)
    print(f"✓ Gerente {nombre} agregado exitosamente")
    return empleados


def agregar_desarrollador(empleados):
    """Agrega un desarrollador"""
    print("\n--- NUEVO DESARROLLADOR ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    lenguaje = input("Lenguaje principal: ")
    horas = int(input("Horas extra (0 si no tiene): "))
    anos_exp = int(input("Años de experiencia: "))

    nuevo = Desarrollador(nombre, edad, salario, lenguaje, horas, 50, anos_exp)
    empleados.append(nuevo)
    print(f"✓ Desarrollador {nombre} agregado exitosamente")
    return empleados


def agregar_practicante(empleados):
    """Agrega un practicante"""
    print("\n--- NUEVO PRACTICANTE ---")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    salario = float(input("Salario base: $"))
    universidad = input("Universidad: ")
    anos_exp = int(input("Años de experiencia: "))

    nuevo = Practicante(nombre, edad, salario, universidad, anos_exp)
    empleados.append(nuevo)
    print(f"✓ Practicante {nombre} agregado exitosamente")
    return empleados


def ver_empleados(empleados):
    """Muestra todos los empleados"""
    if not empleados:
        print("\n△ No hay empleados registrados")
        return

    print("\n" + "=" * 60)
    print("LISTA DE EMPLEADOS")
    print("=" * 60)

    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp.mostrar_info()}")

    print("=" * 60)


def calcular_salario_individual(empleados):
    """Calcula el salario de un empleado específico"""
    if not empleados:
        print("\n△ No hay empleados registrados")
        return

    print("\n--- SELECCIONE EMPLEADO ---")
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp.nombre} ({type(emp).__name__})")

    try:
        opcion = int(input("\nNúmero del empleado: ")) - 1
        if 0 <= opcion < len(empleados):
            emp = empleados[opcion]
            print("\n" + "- " * 40)
            print(emp.mostrar_info())
            print(f"Salario calculado: ${emp.calcular_salario():.2f}")
            print("- " * 40)
        else:
            print("△ Opción inválida")
    except ValueError:
        print("△ Por favor ingrese un número válido")


def aumentar_salario_individual(empleados):
    """Aumenta el salario de un empleado específico"""
    if not empleados:
        print("\n△ No hay empleados registrados")
        return

    print("\n--- SELECCIONE EMPLEADO PARA AUMENTAR SALARIO ---")
    for i, emp in enumerate(empleados, 1):
        print(f"{i}. {emp.nombre} ({type(emp).__name__}) - Salario actual: ${emp.calcular_salario():.2f}")

    try:
        opcion = int(input("\nNúmero del empleado: ")) - 1
        if 0 <= opcion < len(empleados):
            emp = empleados[opcion]
            porcentaje = float(input("Porcentaje de aumento (%): "))
            salario_anterior = emp.calcular_salario()
            nuevo_salario_base = emp.aumentar_salario(porcentaje)
            print(f"\n✓ Salario de {emp.nombre} aumentado exitosamente")
            print(f"  Salario anterior: ${salario_anterior:.2f}")
            print(f"  Nuevo salario: ${emp.calcular_salario():.2f}")
            print(f"  Nuevo salario base: ${nuevo_salario_base:.2f}")
        else:
            print("△ Opción inválida")
    except ValueError:
        print("△ Por favor ingrese un número válido")


def ver_total_nomina(empleados):
    """Muestra el total de la nómina"""
    if not empleados:
        print("\n△ No hay empleados registrados")
        return

    total = sum(emp.calcular_salario() for emp in empleados)
    promedio = total / len(empleados)

    print("\n" + "=" * 50)
    print("RESUMEN DE NÓMINA")
    print("=" * 50)
    print(f"Total empleados: {len(empleados)}")
    print(f"Total nómina: ${total:.2f}")
    print(f"Promedio salario: ${promedio:.2f}")
    print("=" * 50)


if __name__ == "__main__":
    # Lista para almacenar empleados
    empleados = []

    # Agregar algunos empleados de ejemplo
    empleados.append(Empleado("Juan Pérez", 30, 3000, 5))
    empleados.append(Gerente("Ana Gómez", 45, 5000, 2000, "Tecnología", 15))
    empleados.append(Desarrollador("Carlos López", 28, 3500, "Python", 10, 50, 3))
    empleados.append(Practicante("Luis Martínez", 22, 2500, "Universidad Nacional", 0))

    print("\n=== SISTEMA DE EMPLEADOS CON HERENCIA Y POLIMORFISMO ===")
    print("Empleados de ejemplo cargados")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            empleados = agregar_empleado(empleados)
        elif opcion == "2":
            empleados = agregar_gerente(empleados)
        elif opcion == "3":
            empleados = agregar_desarrollador(empleados)
        elif opcion == "4":
            empleados = agregar_practicante(empleados)
        elif opcion == "5":
            ver_empleados(empleados)
        elif opcion == "6":
            calcular_salario_individual(empleados)
        elif opcion == "7":
            aumentar_salario_individual(empleados)
        elif opcion == "8":
            ver_total_nomina(empleados)
        elif opcion == "9":
            print("\n=== ¡Hasta luego! ===")
            break
        else:
            print("\n△ Opción inválida. Intente nuevamente.")
            print("\n△ Opción inválida. Intente nuevamente.")
            print("\n△ Opción inválida. Intente nuevamente.")
            print("\n△ Opción inválida. Intente nuevamente.")