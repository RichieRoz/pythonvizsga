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
        # Ellenőrzés: Dátum érvényessége (jövőbeni)
        if datum < datetime.now():
            print("Hibás dátum. Kérlek, adj meg egy jövőbeni dátumot.")
            return

        # Ellenőrzés: Szoba elérhetősége a megadott dátumon
        foglalhato = True
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                foglalhato = False
                break

        if foglalhato:
            foglalas = Foglalás(szoba, datum)
            self.foglalasok.append(foglalas)
            print("Foglalás sikeresen hozzáadva.")
        else:
            print("Ez a szoba már foglalt ezen a dátumon.")

    def foglalas_datum_alapjan(self, datum):
        foglalt_arak = {}
        for foglalas in self.foglalasok:
            if foglalas.datum == datum:
                szoba = foglalas.szoba
                foglalt_arak[szoba.szobaszam] = szoba.ar
        return foglalt_arak

    def foglalas_lemondas(self, szoba, datum):
        lemondando_foglalas = None
        for foglalas in self.foglalasok:
            if foglalas.szoba == szoba and foglalas.datum == datum:
                lemondando_foglalas = foglalas
                break

        if lemondando_foglalas:
            self.foglalasok.remove(lemondando_foglalas)
            return True
        else:
            return False

    def listaz_foglalasok(self):
        print("Foglalások listája:")
        for foglalas in self.foglalasok:
            print(foglalas.info())

    def info(self):
        print(f"{self.nev} szálloda szobái:")
        for szoba in self.szobak:
            print(szoba.info())
        print("\nFoglalások:")
        for foglalas in self.foglalasok:
            print(foglalas.info())

def main():
    hotel = Szalloda("Hotel")
    szoba1 = Szoba(15000, 101)
    szoba2 = Szoba(25000, 201)

    hotel.add_szoba(szoba1)
    hotel.add_szoba(szoba2)

    while True:
        print("\nVálassz műveletet:")
        print("1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("4. Kilépés")

        valasztas = input("Választásod: ")

        if valasztas == "1":
            szobaszam = input("Add meg a szoba számát: ")
            datum_str = input("Add meg a foglalás dátumát (YYYY-MM-DD): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")

            # Szoba és foglalás hozzáadása
            szoba = next((szoba for szoba in hotel.szobak if szoba.szobaszam == int(szobaszam)), None)
            if szoba:
                hotel.foglalas(szoba, datum)
            else:
                print("Hibás szoba szám.")

        elif valasztas == "2":
            szobaszam = input("Add meg a lemondandó foglalás szoba számát: ")
            datum_str = input("Add meg a lemondandó foglalás dátumát (YYYY-MM-DD): ")
            datum = datetime.strptime(datum_str, "%Y-%m-%d")

            # Foglalás lemondása
            szoba = next((szoba for szoba in hotel.szobak if szoba.szobaszam == int(szobaszam)), None)
            if szoba:
                lemondas_sikeres = hotel.foglalas_lemondas(szoba, datum)
                if not lemondas_sikeres:
                    print("Nincs ilyen foglalás ezen a dátumon és szobaszámon.")
            else:
                print("Hibás szoba szám.")

        elif valasztas == "3":
            hotel.listaz_foglalasok()

        elif valasztas == "4":
            print("Kilépés.")
            break

        else:
            print("Érvénytelen választás. Kérem, válassz újra.")

if __name__ == "__main__":
    main()