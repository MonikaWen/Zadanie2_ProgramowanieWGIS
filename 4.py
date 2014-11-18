class Artysta:
    def __init__(self, imie, nazwisko):
        self.imie=imie
        self.nazwisko=nazwisko
    def get_imie(self):
        return self.__imie
    def set_imie(self,imie):
        self.__imie=imie
    def get_nazwisko(self):
        return self.__nazwisko
    def set_nazwisko(self,nazwisko):
        self.__nazwisko=nazwisko
    def str(self):
        print "imie= " +self.imie+" nazwisko= " +self.nazwisko

class Malarz(Artysta):
    def __init__(self, imie, nazwisko, obraz):
        Artysta.__init__(self, imie, nazwisko)
        self.obraz=obraz
    def nazywam_sie_namalowalem(self):
        print "Nazywam sie "+self.imie+" "+self.nazwisko+" namalowalem " +self.obraz

class Muzyk(Artysta):
    def __init__(self, imie, nazwisko, piosenka):
        Artysta.__init__(self, imie, nazwisko)
        self.piosenka=piosenka
    def nazywam_sie_nagralem(self):
        print "Nazywam sie "+self.imie+" "+self.nazwisko+" nagralem " +self.piosenka

class Malarz_Muzyk(Malarz, Muzyk):
    def __init__(self, imie, nazwisko, obraz, piosenka):
        Artysta.__init__(self, imie, nazwisko)
        Muzyk.__init__(self, imie, nazwisko, piosenka)
        Malarz.__init__(self, imie, nazwisko, obraz)
    def nazywam_sie_namalowalem_nagralem(self):
        print "Nazywam sie "+self.imie+" "+self.nazwisko+" namalowalem " +self.obraz+" nagralem " +self.piosenka
        
Janek = Artysta("Jan","Matejko")
Janek.str()
Zbyszek = Muzyk("Zbychu", "Pierzyna", "majteczki w kropeczki")
Zbyszek.nazywam_sie_nagralem()
Bozydar = Malarz_Muzyk("Bozydar", "Iwanow", "Bitwa", "husia siusia")
Bozydar.nazywam_sie_namalowalem_nagralem()