"""Scrivete una funzione di nome usa_solo che richieda una parola e una stringa di
lettere, e che restituisca True se la parola contiene solo le lettere indicate. Riuscite a comporre una
frase in inglese usando solo le lettere acefhlo? Diversa da “Hoe alfalfa”?"""


def usa_solo(parola, lettere):
    for lettera in parola:
        if lettera not in lettere:
            return False
    return True


def main():
    print(usa_solo("ciao", "cioaqq"))


if __name__ == "__main__":
    main()