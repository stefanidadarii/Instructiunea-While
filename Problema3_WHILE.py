#Se citesc numere de la tastatură până la introducerea unui număr impar divizibil cu 3. Să se afişeze suma tuturor numerelor pare introduse.
x=eval(input('introduceti un numar: '))
s=0
while not((x%2!=0) and (x%3==0)):
    if x%2==0:
        s+=x
    x=eval(input('introduceti un numar: '))

print('Suma numerelo pare este ', s)