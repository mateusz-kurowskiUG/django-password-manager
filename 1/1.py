with open("file.txt", "r") as file:
    lines = file.readlines()

lista = [1, 2, 3, 4, 5]
lista2 = lista[:]  # robi kopię tak jak lista.copy()


dict = {"name": "Kauricio", "surname": "Schmitz", "age": None}


print(dict.get("name", None)) #bierze dict["name"], w razie niepowodzenia zwraca None


try:
    print(dict["date"])
except KeyError:
    print("brak takiego klucza")


print(dict.setdefault("date", None)) #nie robi nic, w razie braku dict["date"] ustawia "date":None
print(dict["date"])


