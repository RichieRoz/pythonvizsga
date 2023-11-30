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

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def info(self):
        print(f"{self.nev} szálloda szobái:")
        for szoba in self.szobak:
            szoba.info()

# Példányosítás és használat
hotel = Szalloda("Luxury Hotel")
egyagyas_szoba = EgyagyasSzoba(101)
ketagyas_szoba = KetagyasSzoba(201)

hotel.add_szoba(egyagyas_szoba)
hotel.add_szoba(ketagyas_szoba)

hotel.info()