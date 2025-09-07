# Matriz 3D: [ciudad][semana][día]
# Supongamos 3 ciudades, 2 semanas y 7 días por semana

import random

# Definir dimensiones
ciudades = ["Santa Elena", "Guayaquil", "El Oro"]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 2

# Crear matriz 3D con temperaturas aleatorias entre 10 y 35 grados
temperaturas = [
    [  # por cada ciudad
        [random.randint(10, 35) for _ in dias]  # por cada día
        for _ in range(semanas)  # por cada semana
    ]
    for _ in ciudades
]

# Calcular promedio de temperaturas por ciudad y semana
for i, ciudad in enumerate(ciudades):
    print(f"\nCiudad: {ciudad}")
    for s in range(semanas):
        suma = 0
        for d in range(len(dias)):
            suma += temperaturas[i][s][d]
        promedio = suma / len(dias)
        print(f"  Semana {s+1}: promedio = {promedio:.2f}°C")
