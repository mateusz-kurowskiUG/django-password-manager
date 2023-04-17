def funk(liczba, ile_razy):
    print(liczba * ile_razy)


slownik = {"liczba": 5, "ile_razy": 2}

funk(**slownik)


def int_to_string(num: int) -> str:
    return str(num)
