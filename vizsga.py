from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def info(self):
        pass

# Példa leszármazott osztály készítésére
class StandardSzoba(Szoba):
    def info(self):
        print(f"Standard szoba #{self.szobaszam}, ár: {self.ar} Ft")

# Példányosítás és használat
standard_szoba = StandardSzoba(20000, 101)
standard_szoba.info()