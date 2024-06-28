from funciones import *


menup = ['Ver listado de pinturas',
         'Buscar pinturas',
         'Agregar pintura',
         'Elimiar pintura',
         'Exportar pinturas',
         'Salir']
while True:
    for ind, opt in enumerate(menup):
        print(f'{ind + 1}. {opt}')
    ans = input('Ingrese una opción:\n')

    if ans == '1':
        ver_pinturas()

    elif ans == '2':
        buscar_pintura() 
    elif ans == '3':
        agregar_pintura()

    elif ans == '4':
        pass
    elif ans == '5':
        exportar_pintura()

    elif ans == '6':
        salir()
    else:
        print('ERROR INESPERADO!!')