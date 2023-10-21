# Abre el archivo de entrada en modo binario
with open('rockyou.txt', 'rb') as entrada:
    # Crea un diccionario vacío para almacenar las contraseñas modificadas
    contraseñas_modificadas = {}

    # Lee línea por línea
    for linea in entrada:
        try:
            # Decodifica la línea utilizando UTF-8
            linea = linea.decode('utf-8').strip()

            # Verifica si la línea comienza con una letra
            if len(linea) > 0 and linea[0].isalpha():
                # Capitaliza la primera letra y agrega un '0' al final
                contraseña_modificada = linea[0].upper() + linea[1:] + '0'
                contraseñas_modificadas[linea] = contraseña_modificada
        except UnicodeDecodeError:
            # Ignora las líneas que no se pueden decodificar
            pass

# Abre el archivo de salida con la codificación adecuada
with open('rockyou_mod.dic', 'w', encoding='utf-8') as salida:
    # Escribe las contraseñas modificadas en el archivo de salida
    for contraseña_modificada in contraseñas_modificadas.values():
        salida.write(contraseña_modificada + '\n')

# Imprime la cantidad de contraseñas en el nuevo archivo
print(f'Se han modificado {len(contraseñas_modificadas)} contraseñas.')

