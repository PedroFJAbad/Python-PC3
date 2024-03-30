import Problema8

# Generar números aleatorios
numeros = Problema8.generar_numeros_aleatorios()

# Mostrar la lista obtenida
Problema8.mostrar_lista(numeros)

# Ordenar los valores de la lista y mostrarla
numeros_ordenados = Problema8.ordenar_lista(numeros)
print("\nLista ordenada:")
Problema8.mostrar_lista(numeros_ordenados)