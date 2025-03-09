import random

# Definir dimensiones de la matriz
ciudades = ["Quito", "Guayaquil", "Cuenca"]
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2  # Número de semanas

# Crear una matriz 3D con temperaturas aleatorias entre 10 y 35 grados Celsius
temperaturas = [[[random.randint(10, 35) for _ in dias_semana] for _ in range(semanas)] for _ in ciudades]

# Calcular y mostrar el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"Promedio de temperaturas para {ciudad}:\n")
    for semana in range(semanas):
        promedio = sum(temperaturas[i][semana]) / len(dias_semana)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()
