"""Leggete la documentazione dei metodi delle stringhe sul sito http: // docs. python. org/ 3/ library/ stdtypes.
html# string-methods . Fate degli esperimenti con alcuni metodi per assicurarvi di avere capito come funzionano.
strip e replace sono particolarmente utili. La documentazione utilizza una sintassi che può risultare poco chiara.
Per esempio, in find(sub[, start[, end]]), le parentesi quadre indicano dei parametri opzionali (non vanno digitate).
Quindi sub è obbligatorio, ma start è opzionale, e se indicate start, allora end è a sua volta opzionale"""


def main():
    s1 = "Ciao mondo!"
    ris1 = s1.replace("mondo", "universo")
    print(f"frase1: {s1}\noutout replace: {ris1}\n")

    s2 = "   Ciao, come stai?   "
    ris2 = s2.strip()
    print(f"frase2: {s2}\noutout strip: {ris2}")

    s3 = "ciao"
    ris3 = s3.upper()
    print(f"frase3: {s3}\noutout upper: {ris3}")


if __name__ == "__main__":
    main()
