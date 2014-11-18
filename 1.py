plik = open("tekst.txt","r") 
plik2=open("statystyki.txt","a")
znaki = plik.read()
print znaki

lista=[]
slowa=znaki.split(" ")
#print slowa

slownik = dict( zip( slowa, slowa ) )

for slowo in slowa:
   slownik[slowo] = slowa.count(slowo)
       
wystapienia_slow = [key for [key, value] in slownik.items()]
liczba_wystapien = [value for [key, value] in slownik.items()]

slownik_wynik = dict( zip( wystapienia_slow, liczba_wystapien ) )

print slownik_wynik

plik2.writelines("Liczba wystapien wyrazu:\n");
plik2.writelines("\n");
plik2.writelines(str(slownik_wynik));
print "Rezultaty w pliku statystyki"
plik.close()
plik2.close()