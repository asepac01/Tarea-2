# number = 96
# if type(number) == int:
#     print("» Resultado:", number * 2)
# else:
#     print("» Este dato NO es numérico.")

# def mensaje(hombre):
#     print(hombre)


# mensaje("  ¤ Mi primer programa.")
# mensaje("  ¤ Mi segundo programa.")


# class Sintaxis:
#     def usoDeVariables(self):
#         edad, _peso = 45, 50.75
#         print("» Edad: {}".format(edad))
#         print("» Peso: {}".format(_peso))


# ejercicio2 = Sintaxis()
# ejercicio2.usoDeVariables()


class Sintaxis:
    iterador = 0
    def __init__(self, dato = "¤ Inicio..."):
        self.palabra = dato

    def usoDeVariables(self):
        edad, _peso = 20, 53.35
        nombre = "Lorely Sepa"
        tipoSex = "Femenino"
        civil = True
        print("  » Nombre: {}".format(nombre))
        print("  » Edad: {}".format(edad))
        print("  » Tipo de Sexo: {}".format(tipoSex))
        print("  » Estado Civil: {}".format(civil))
        print("  » Peso: {}".format(_peso))


ejercicio3 = Sintaxis()
print(ejercicio3.palabra)
ejercicio3.usoDeVariables()
