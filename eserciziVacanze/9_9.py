"""“Di recente ho fatto visita a mia madre, e ci siamo accorti che le due cifre che compongono la mia età, invertite,
formano la sua. Per esempio, se lei avesse 73 anni, io ne avrei 37. Ci siamo domandati quanto spesso succedesse
questo negli anni, ma poi abbiamo divagato su altri discorsi senza darci una risposta.” “Tornato a casa, ho calcolato
che le cifre delle nostre età sono state sinora invertibili per sei volte. Ho calcolato anche che se fossimo
fortunati succederebbe ancora tra pochi anni, e se fossimo veramente fortunati succederebbe un’altra volta ancora. In
altre parole, potrebbe succedere per 8 volte in tutto. La domanda è: quanti anni ho io in questo momento?” Scrivete
un programma in Python che ricerchi la soluzione a questo quesito. Suggerimento: potrebbe esservi utile il metodo
delle stringhe zfill."""


def isPalindromo(valore1, valore2):
    a = str(valore1).zfill(2)
    b = str(valore2).zfill(2)
    # print(a, b)
    if a[::-1] == b:
        return True
    return False


def trovaEtaPalindrome(gap):
    for i in range(0, 99):
        if isPalindromo(i, i + gap):
            print(i, i + gap)


def main():
    # print(isPalindromo("12", "21"))
    gap = 73 - 37
    # print(gap)
    trovaEtaPalindrome(gap)


if __name__ == "__main__":
    main()
