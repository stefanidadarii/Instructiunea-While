#Se citesc pe rând temperaturile medii ale fiecărei luni a unui an, ca numere întregi. Să se afişeze cu două zecimale media anuală a temperaturilor pozitive şi a celor negative. 
suma_p=0
suma_n=0
nr_p=0
nr_n=0
l=1
while l<=12:
    t=eval(input('Introduceti temperatura: '))
    if t>=0:
        suma_p+=t
        nr_p+=1
    if t<0:
        suma_n+=t 
        nr_n+=1
    l+=1

print('Media anuală a temperaturilor pozitive este ', round(suma_p/nr_p, 2), ', iar media anuală a temperaturilor negative este ', round(suma_n/nr_n, 2))   