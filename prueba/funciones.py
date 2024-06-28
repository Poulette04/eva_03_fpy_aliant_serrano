import csv 

pinturas = []
codigo = [380560]
def agregar_pintura():
    print('AGREGAR PINTURAS')
    nombre = input('Ingrese el nombre del color:\n')
    tipo = input('Ingrese el tipo, acrilico o latex:\n')
    valor = int(input('Ingrese precio de la pintura:\n'))
    stock = int(input('Ingrese el stock:\n'))
    pintura = {'nombre': nombre, 'tipo': tipo, 'valor': valor, 'stock': stock}
    pinturas.append(pintura)
    
    print('PINTURA AGREGADA CON EXITO!!')

def ver_pinturas():
    if not pinturas:
        print('No hay pinturas, por favor agregar pintura')
    else:
        for p in pinturas:
            print('Nombre:',p['nombre'])
            
            


def exportar_pintura():
    nombre = 'mandarina.csv'
    with open(nombre, mode='w', newline='')as archivo:
        writer = csv.writer(archivo)
        writer.writerow(nombre)

def salir():
    print('Gracias por usar el programa, Adiositoo!')
    exit()

def buscar_pintura():
    if not pinturas:
        print('No hay pinturas, agrega na por favor')
    else:
        
        nombre= input('Ingresa el nombre de la pintura buscar')
        for p in pinturas:
            if nombre.lower() == 
