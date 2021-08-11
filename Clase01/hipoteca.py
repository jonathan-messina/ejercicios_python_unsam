# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca


saldo = 500000.0
tasa = 0.05
mes = 0
pago_mensual = 2684.11
pago_mensual_fijo = 2684.11
total_pagado = 0.0
pago_extra_mes_comienzo = 61
pago_extra_mes_final = 108
pago_extra = 1000


while saldo > 0:
    # se añade la condicion a los primeros 12 meses
    # while mes <= 12:
    #     pago_mensual = pago_mensual_fijo
    #     pago_mensual = pago_mensual + pago_extra
    #     saldo = saldo * (1+tasa/12) - pago_mensual
    #     total_pagado = total_pagado + pago_mensual
    #     mes += 1
    #     print(pago_mensual)
    #     print(mes, round(total_pagado, 4), round(saldo, 4))
    # se aplica la condicion pasados los 6 años de empezada la hipoteca
    while mes >= pago_extra_mes_comienzo and mes <= pago_extra_mes_final:
        pago_mensual = pago_mensual_fijo
        pago_mensual = pago_mensual + pago_extra
        saldo = saldo * (1+tasa/12) - pago_mensual
        total_pagado = total_pagado + pago_mensual
        mes += 1
        print(mes, round(total_pagado, 4), round(saldo, 4))
    # iteracion normal inicial
    pago_mensual = pago_mensual_fijo
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
    mes += 1
    print(mes, round(total_pagado, 4), round(saldo, 4))
    # se ajusta el ultimo mes al valor restante
    if saldo <= pago_mensual_fijo:
        pago_mensual_fijo = saldo
        saldo = saldo - pago_mensual_fijo
        total_pagado = total_pagado + saldo
        mes += 1
        print(mes, round(total_pagado, 4), round(saldo, 4))


print('Total pagado: ', round(total_pagado, 2), '.', sep='')
print('Meses: ', mes, '.', sep='')
