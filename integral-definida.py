from sympy import integrate
from sympy.abc import x

funcion2= x**2 + 5  # función a integrar
resultado= integrate(funcion2, (x, 0, 2) # el metodo integrate lleva como parametros la función a integrar, la variable de integración (x) y los límites inferior y superior( en este caso es 0 y 2 de acuerdo a lo establecido en el ejercicio)
print("El resultado es: ", resultado)
                     
