def leap_year():
    my_year=int(input("Ingrese un año: "))
    if ((my_year%4 == 0) and (my_year%100 !=0)):
        print(f"El año {my_year} es bisiesto")
    elif ((my_year%100==0) and (my_year%400==0)):
        print(f"El año {my_year} es bisiesto")
    else:
        print(f"El año {my_year} no es bisiesto")
