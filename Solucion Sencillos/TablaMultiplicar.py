'''
/*
 * Escribe un programa que muestre la tabla de multiplicar
 * introducido por parámetro
 */
'''
numero_tabla = int(input("Eliga el numero para hacer su tabla: "))

for item in range(1, 11):
    print("{} x {} = {}".format(item, numero_tabla, item * numero_tabla))


