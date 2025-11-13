import random

CISLO_DELKA: int = 4
ODDELOVAC: str = "-" * 40


def pozdrav_uzivatele():
    print(f"Hi there!\n{ODDELOVAC}")
    print(f"I've generated a random {CISLO_DELKA} digit number for you.")
    print(f"Let's play a bulls and cows game.")


def generuj_tajne_cislo() -> str:
    prvni_cislo = str(random.randint(1, 9))
    zbytek_cisel = [str(i) for i in range(10) if str(i) != prvni_cislo]
    random.shuffle(zbytek_cisel)

    tajne_cislo = prvni_cislo + "".join(zbytek_cisel[:CISLO_DELKA - 1])
    return tajne_cislo


def ziskej_hadani() -> str:
    print(ODDELOVAC)
    print("Enter a number:")
    print(ODDELOVAC)
    return input(">>> ")


def validuj_hadani(hadani: str) -> str | None:
    if not hadani.isnumeric():
        return "Your guess must contain only numbers."
    if len(hadani) != CISLO_DELKA:
        return f"Your guess must be {CISLO_DELKA} digits long."
    if hadani[0] == '0':
        return "Your guess must not start with zero."
    if len(set(hadani)) != CISLO_DELKA:
        return "Your guess must not contain duplicate digits."
    return None


def spocitej_bulls_cows(tajne: str, hadani: str) -> tuple[int, int]:
    bulls = sum(1 for i in range(CISLO_DELKA) if tajne[i] == hadani[i])
    
    cows = 0
    for c in set(hadani):
        if c in tajne:
            cows += min(hadani.count(c), tajne.count(c))

    return bulls, (cows - bulls)


def vypis_vysledek(bulls: int, cows: int):
    bull_str = "bull" if bulls == 1 else "bulls"
    cow_str = "cow" if cows == 1 else "cows"
    print(f"{bulls} {bull_str}, {cows} {cow_str}")


def hlavni():
    pozdrav_uzivatele()
    tajne_cislo = generuj_tajne_cislo()
    pocet_pokusu = 0

    while True:
        hadani = ziskej_hadani()
        pocet_pokusu += 1
        
        chyba = validuj_hadani(hadani)
        if chyba:
            print(chyba)
            continue

        bulls, cows = spocitej_bulls_cows(tajne_cislo, hadani)

        if bulls == CISLO_DELKA:
            print(f"Correct, you've guessed the right number")
            print(f"in {pocet_pokusu} guesses!")
            print(ODDELOVAC)
            print("That's amazing!")
            break
        else:
            vypis_vysledek(bulls, cows)


if __name__ == "__main__":
    hlavni()