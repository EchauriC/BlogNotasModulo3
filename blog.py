'''
    Blog de Notas de (C Echauri)
    -----------------------------

'''


notas = []

#### Interfaz ####
def mostrarMenu():

    print('''
    TU BLOG DE NOTAS PERSONAL

        Menu
            [1] Ver Notas
            [2] Crear Nota
            [3] Editar nota
            [4] Borrar nota
            [5] Buscar en notas
            [0] Salir
            
    ''')


#### Control de flujo ####
def accionMenu(opcion):

    global notas

    if opcion < 1 or opcion > 5:
        print('Opcion no disponible')
    else:

        if opcion == 2:
            while True:
                crearNota(notas)
                if not repetirAccion():
                    break

        elif opcion == 5:
            while True:
                if existenNotas(notas):
                    buscarEnNotas(notas)
                    if not repetirAccion():
                        break
                else:
                    break
        else:
            while True:
                if existenNotas(notas):
                    mostrarNotas(notas)

                    if opcion != 1:
                        seleccion = seleccionarNota()

                        if existeNota(seleccion,notas):
                            if opcion == 3:
                                editarNota(seleccion, notas)
                            elif opcion == 4:
                                borrarNota(seleccion, notas)
                        else:
                            print('La nota seleccionada no existe')

                        if not repetirAccion():
                            break
                    else:
                        break
                else:
                    break

        if opcion not in [1,5]:
            guardarNotas(notas)


def repetirAccion():
    try:
        repetir = int(input('¿Quieres repetir el proceso? 1 = Si / Otra tecla = continuar: '))
    except ValueError as identifier:
        repetir = -1

    if repetir == 1:
        return True
    else:
        return False


#### Acciones sobre las notas como escritura, lectura, etc ####
def crearNota(notas):
    texto = input('Introduce la nueva nota: ')
    notas.append(texto)
    print(f'Nota añadida')
    print('')


def mostrarNotas(notas):
    for idx, nota in enumerate(notas):
        print(f'[{idx}] -> {nota}')


def seleccionarNota():
    try:
        seleccion = int(input('Selecciona una nota introduciendo su número: '))
    except ValueError as identifier:
        seleccion = -1

    return seleccion


def editarNota(seleccion, notas):
    notas[seleccion] = input(f'Introduce el nuevo texto para la nota {seleccion}: ')
    print(f'Nota {seleccion} modificada')
    print('')


def borrarNota(seleccion, notas):
    del notas[seleccion]
    print(f'Nota {seleccion} eliminada')
    print('')


def buscarEnNotas(notas):
    filtro = input('Introduce lo que quieras buscar: ')
    count = 0
    for idx, nota in enumerate(notas):
        if nota.count(filtro) > 0:
            print(f'[{idx}] -> {nota}')
            count += 1
    if count == 0:
        print(f'No hay notas que contengan ese texto.')


#### Lectura y escritura de archivos ####
def crearArchivo():
    print('Creando archivo blog.txt...')
    file = open('blog.txt', 'w')
    file.close()
    print('Archivo creado.')
    print('')


def cargarNotas(notas):
    print('Cargando notas...')
    with open('blog.txt', 'r') as file:
        for linea in file:
            if linea != f'\n' and linea != '':
                notas.append(linea)

    if existenNotas(notas):
        print('Notas cargadas.')
        print('')


def guardarNotas(notas):
    print(f'Guardando cambios...')

    with open('blog.txt', 'w') as file:
        for nota in notas:
            file.write(f'{nota}\n')
        file.close()

    print(f'Cambios aplicados.')
    print('')


#### Comprobaciones sobre archivos y variables ####
def existeArchivo():
    try:
        print('Comprobando si existe el archivo blog.txt...')
        file = open('blog.txt', 'r')
        file.close()
        print('Archivo encontrado.')
        print('')

        return True

    except FileNotFoundError as identifier:
        print('No se ha encontrado el archivo.')
        print('')

        return False


def existenNotas(notas):
    if len(notas) == 0:
        print('No hay notas guardadas.')
        print('')
        return False
    else:
        return True


def existeNota(seleccion, notas):
    if seleccion < 0:
        return False

    if len(notas) > seleccion:
        return True
    else:
        return False


#### Inicializar la app ####
def run():

    # Si no existe el arhcivo lo creamos, sino leemos archivo
    if not existeArchivo():
        crearArchivo()
    else:
        cargarNotas(notas)

    # Mantiene al usuario en la interfaz hasta que indica "salir"
    while True:

        mostrarMenu()

        try:
            opcion = int(input('Opcion: '))
        except ValueError as identifier:
            opcion = -1
        print('')

        if opcion == 0:
            break

        accionMenu(opcion)


#### App launcher ####
if __name__ == "__main__":
    run()
