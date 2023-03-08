print("Por favor introduce los kilómetros recorridos por una moto y la cantidad de litros consumidos")
kilometrosUser = float(input("Kilometros recorridos: "))
litrosUser = float(input("Litros de combustible gastados: "))
if kilometrosUser == 0 or litrosUser ==0:
    print("No es posible calcular el consumo de combustible por kilometro por que uno de los datos es 0")
else:
    consumoKilometro=kilometrosUser/litrosUser
    print(f"El consumo por kilómetro es de {str(consumoKilometro)}")