def solicitar_fraccion():
    while True:
        try:
            fraccion = input("Ingrese una fracción en formato X/Y: ")
            x, y = map(int, fraccion.split('/'))
            if x <= 0 or y <= 0:
                raise ValueError
            if x > y:
                raise ValueError
            return x, y
        except ValueError:
            print("La fracción debe ser en formato X/Y, donde X e Y son enteros positivos, y X <= Y.")


def calcular_porcentaje(x, y):
    porcentaje = (x / y) * 100
    if porcentaje < 1:
        return 'E'
    elif porcentaje > 99:
        return 'F'
    else:
        return f'{round(porcentaje)}%'


def main():
    while True:
        try:
            x, y = solicitar_fraccion()
            print(f"La cantidad de combustible en el tanque es: {calcular_porcentaje(x, y)}")
            break
        except ZeroDivisionError:
            print("El denominador no puede ser cero. Por favor, ingrese una fracción válida.")
        except ValueError:
            print("La fracción debe ser en formato X/Y, donde X e Y son enteros positivos, y X <= Y.")


if __name__ == "__main__":
    main()