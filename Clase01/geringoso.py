# geringoso.py
# Archivo de ejemplo
# Ejercicio de geringoso


cadena = 'Geringoso'
listacadena = list(cadena)
capadepenapa = ''
for i, c in enumerate(listacadena):
    if listacadena[i] == 'a':
        listacadena[i] = 'apa'
    if listacadena[i] == 'e':
        listacadena[i] = 'epe'
    if listacadena[i] == 'i':
        listacadena[i] = 'ipi'
    if listacadena[i] == 'o':
        listacadena[i] = 'opo'
    if listacadena[i] == 'u':
        listacadena[i] = 'upu'
cadena = ''.join(listacadena)
print(cadena)
