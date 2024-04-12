import math
def line():
    A=float(input("Ingrese el coeficiente A: "))

    B=float(input("Ingrese el coeficiente B: "))

    X1=float(input("Ingrese el coeficiente x1: "))

    X2=float(input("Ingrese el coeficiente x2: "))    

    Y1=(A*X1+B)
    Y2=(A*X2+B)

    P1=(X1, Y1)
    P2=(X2, Y2)

    Distance = math.dist(P1,P2)

    print("El coeficiente A de su ecuación de la recta es:", A)
    print("El coeficiente B de su ecuación de la recta es:", B)
    print("El coeficiente X1 de su ecuación de la recta es:", X1)
    print("El coeficiente X2 de su ecuación de la recta es:", X2)
    print()
    print(f"""Para la siguiente ecuación:
\tY = {A}X + {B}""") 
    print()
    print(f"""Dados los siguientes puntos:
\tP1 {X1, Y1}
\tP2 {X2, Y2}""")
    print()
    print(f"La distancia entre ellos es: {Distance}")
