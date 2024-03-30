class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print(f"Nombre: {self.nombre}")
        print(f"Número de Registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"Nota {i}: {nota}")
    
    def setAge(self, edad):
        self.edad = edad

    def setNota(self, notas):
        self.notas = notas

# Ejemplo de uso
nombre = input("Ingrese el nombre del alumno: ")
numero_registro = input("Ingrese el número de registro del alumno: ")
alumno = Alumno(nombre, numero_registro)
edad = int(input("Ingrese la edad del alumno: "))
alumno.setAge(edad)
notas = []
while True:
    try:
        nota = float(input("Ingrese una nota del alumno (o ingrese 'fin' para terminar): "))
        notas.append(nota)
    except ValueError:
        break
alumno.setNota(notas)
alumno.display()