from datetime import datetime

class Szoba:
    def __init__(self, ar, szobaszam):
        self.ar = ar
        self.szobaszam = szobaszam

    def info(self):
        return f"Szoba #{self.szobaszam}, ár: {self.ar} Ft"

class Foglalás:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

    def info(self):
        return f"Foglalás dátuma: {self.datum.strftime('%Y-%m-%d')}\n{self.szoba.info()}"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def add_szoba(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szoba, datum):
        foglalas = Foglalás(szoba, datum)
        self.foglalasok.append(foglalas)

    def foglalas_datum_alapjan(self, datum):
        foglalt_arak = {}
        for foglalas in self.foglalasok:
            if foglalas.datum == datum:
                szoba = foglalas.szoba
                foglalt_arak[szoba.szobaszam] = szoba.ar
        return foglalt_arak

    def info(self):
        print(f"{self.nev} szálloda szobái:")
        for szoba in self.szobak:
            print(szoba.info())
        print("\nFoglalások:")
        for foglalas in self.foglalasok:
            print(foglalas.info())

# Példányosítás és használat
hotel = Szalloda("Luxury Hotel")
szoba1 = Szoba(15000, 101)
szoba2 = Szoba(25000, 201)

hotel.add_szoba(szoba1)
hotel.add_szoba(szoba2)

hotel.foglalas(szoba1, datetime(2023, 12, 1))
hotel.foglalas(szoba2, datetime(2023, 12, 2))
hotel.foglalas(szoba1, datetime(2023, 12, 1))  # Még egy példa foglalás ugyanarra a dátumra

# Foglalások lekérdezése dátum alapján
foglalt_arak = hotel.foglalas_datum_alapjan(datetime(2023, 12, 1))
print(f"Foglalt árak a 2023-12-1 dátumra: {foglalt_arak}")

hotel.info()