plik = open("menu.txt","r") 
znaki = plik.read()
znaki = znaki.replace("\n", " ")
znaki = znaki.split(" ")
menu_zamowienia={}
print znaki

dlugosc=len(znaki)

i=0

while i<dlugosc:
    menu_zamowienia[znaki[i]]=float(znaki[i+1])
    i=i+2 

print menu_zamowienia

def zamowienie(zamowienie):
    cena = 0
    napiwek=0
    for i in zamowienie:
        if i in menu_zamowienia:
            cena+=menu_zamowienia[i]
        napiwek=0.1*cena
        
    print "Cena: " +str(cena)+" napiwek: " + str(napiwek) 
    return cena + napiwek
zamowienie(["pizza","herbata"])

plik.close()

