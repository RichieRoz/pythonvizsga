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

from abc import ABC, abstractmethod

class Szoba(ABC):
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    @abstractmethod
    def info(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(15000, szobaszam)
        self.egyagyas_agy = True

    def info(self):
        print(f"Egyágyas szoba #{self.szobaszam}, ár: {self.ar} Ft, egyágyas ágy: {self.egyagyas_agy}")

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(25000, szobaszam)
        self.ketagyas_agy = True

    def info(self):
        print(f"Kétágyas szoba #{self.szobaszam}, ár: {self.ar} Ft, kétágyas ágy: {self.ketagyas_agy}")

# Példányosítás és használat
egyagyas_szoba = EgyagyasSzoba(201)
ketagyas_szoba = KetagyasSzoba(302)

egyagyas_szoba.info()
ketagyas_szoba.info()