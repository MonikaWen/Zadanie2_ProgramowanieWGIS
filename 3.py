import math
zespolona1=(1,5)
zespolona2=(3,5)
def dodaj(z1, z2):
 return (z1[0]+z2[0],z1[1]+z2[1])
def odejmij(z1, z2):
    return(z2[0]-z1[0],z2[1]-z2[1])
def modul(z):
 return math.sqrt(z[0]**2+z[1]**2)
def drukuj_zespolona(z):
 return str(z[0])+" + "+str(z[1])+"i"

suma = dodaj(zespolona1, zespolona2)
roznica = odejmij(zespolona1, zespolona2)
wartosc_modulu = modul(zespolona1)
pokaz_liczbe_zespolona = drukuj_zespolona(zespolona1)
print suma
print roznica
print wartosc_modulu
print pokaz_liczbe_zespolona