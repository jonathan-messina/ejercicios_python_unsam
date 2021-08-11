# rebotes.py
# Archivo de ejemplo
# Ejercicio

altura = 100
x = range(1, 11)

for n in x:
    rebote = round(float(altura * 0.6), 4)
    altura = rebote
    print(n, ' ', rebote)
