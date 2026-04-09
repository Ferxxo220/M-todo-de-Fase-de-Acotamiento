import math

class MetodoFaseAcotamiento:
    """
    Clase que implementa el algoritmo de acotamiento para encerrar un mínimo.
    """

    @staticmethod
    def optimizar(f, x0, delta):
        
        delta = abs(delta)  
        f_izq = f(x0 - delta)
        f_centro = f(x0)
        f_der = f(x0 + delta)

        if f_izq >= f_centro >= f_der:
            d = delta
        elif f_izq <= f_centro <= f_der:
            d = -delta
        elif f_izq >= f_centro and f_der >= f_centro:
            
            return sorted([x0 - delta, x0 + delta])
        else:
            return "No se cumple la condición de función unimodal en este punto."

        
        k = 0
        puntos = [x0]
        
        
        puntos.append(puntos[k] + (2**k) * d)

        while f(puntos[-1]) < f(puntos[-2]):
            k += 1
            
            nuevo_x = puntos[-1] + (2**k) * d
            puntos.append(nuevo_x)

        
        if len(puntos) < 3:
            
            return sorted([puntos[0], puntos[-1]])
            
        a = puntos[-3]
        b = puntos[-1]
        
        return sorted([a, b])




f1 = lambda x: math.exp(x) - 5*x
f2 = lambda x: x**4 - 3*x**3 + 2
f3 = lambda x: x**2 - math.log(x)

pruebas = [
    {"nombre": "1. Exponencial", "f": f1, "x0": 0.0, "delta": 0.5},
    {"nombre": "2. Polinomial", "f": f2, "x0": 0.0, "delta": 0.1},
    {"nombre": "3. Logarítmica", "f": f3, "x0": 0.5, "delta": 0.2},
]

print(f"{'Función':<20} | {'x0':<5} | {'Delta':<5} | {'Intervalo [a, b]'}")
print("-" * 65)

for p in pruebas:
    resultado = MetodoFaseAcotamiento.optimizar(p["f"], p["x0"], p["delta"])
    print(f"{p['nombre']:<20} | {p['x0']:<5} | {p['delta']:<5} | {resultado}")