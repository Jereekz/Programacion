#ingresar cantidad del producto
cantidad = int(input("Ingrese la cantidad de productos: "))
#calcular el siguiente
siguiente = ((cantidad // 100) + 1) * 100
#total de siguiente centena
print("La siguiente centena completa mayor es:", siguiente)