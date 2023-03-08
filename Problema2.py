print("Por favor introduce el precio del producto")
precioProducto = float(input("Precio del producto: ")) 
if precioProducto ==0:
    print("No es posible calcular el precio del producto por que introdujo 0")
else:
    precioProductoTotal=precioProducto*0.85
    print(f"Precio total con descuento {str(precioProductoTotal)}")