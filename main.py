import os

def file_exists(file):
    """Verifica si un archivo existe."""
    return os.path.isfile(file)

def get_phone(file, client):
    """Devuelve el teléfono de un cliente de un fichero dado."""
    if file_exists(file):
        with open(file, 'r') as f:
            for line in f:
                name, phone = line.strip().split(',')
                if name == client:
                    return phone
        return f"No se encontró el teléfono para el cliente '{client}'."
    else:
        return f"Error: El fichero '{file}' no existe."

def add_phone(file, client, telf):
    """Añade el teléfono de un cliente de un fichero dado."""
    if file_exists(file):
        with open(file, 'a') as f:
            f.write(f"{client},{telf}\n")
        return f"Teléfono de {client} añadido correctamente."
    else:
        return f"Error: El fichero '{file}' no existe."

def remove_phone(file, client):
    """Elimina el teléfono de un cliente de un fichero dado."""
    if file_exists(file):
        with open(file, 'r') as f:
            lines = f.readlines()

        with open(file, 'w') as f:
            for line in lines:
                name, _ = line.strip().split(',')
                if name != client:
                    f.write(line)
        return f"Teléfono de {client} eliminado correctamente."
    else:
        return f"Error: El fichero '{file}' no existe."

def create_directory(file):
    """Crea un fichero vacío para guardar un listín telefónico."""
    try:
        with open(file, 'w'):
            pass
        return f"Fichero '{file}' creado correctamente."
    except IOError:
        return f"Error al crear el fichero '{file}'."

def menu():
    """Presenta un menú con las operaciones disponibles sobre un listín telefónico."""
    print('Gestión del listín telefónico')
    print('============================')
    print('1 - Consultar un teléfono')
    print('2 - Añadir un teléfono')
    print('3 - Eliminar un teléfono')
    print('4 - Crear el listado')
    print('0 - Terminar')
    option = input('Introduzca el número de la opción deseada: ')
    return option

def directory():
    """Lanza la aplicación para la gestión del listín telefónico."""
    file = 'listado.txt'
    while True:
        option = menu()
        if option == '1':
            name = input('Introduce el nombre del cliente: ')
            print(get_phone(file, name))
        elif option == '2':
            name = input('Introduce el nombre del cliente: ')
            telf = input('Introduce el teléfono del cliente: ')
            print(add_phone(file, name, telf))
        elif option == '3':
            name = input('Introduce el nombre del cliente: ')
            print(remove_phone(file, name))
        elif option == '4':
            print(create_directory(file))
        elif option == '0':
            break
        else:
            print('Opción no válida. Por favor, seleccione una opción válida.')


directory()







