secret_number = 777

print(
"""
+==================================+
| Benvenuto nel mio gioco, babbano!|
| Immettere un numero intero       |
| e indovina che numero ho         |
| scelto per te.                   |
| Allora, qual è il numero segreto?|
+==================================+
"""
)

# Ottieni il primo input dell'utente
number = int(input("Immetti un numero: "))

# Ciclo che continua fino a quando l'utente non indovina il numero
while number != secret_number:
    print("Ha ha! Sei bloccato nel mio loop!")
    # Chiedi all'utente di inserire nuovamente un numero
    number = int(input("Prova di nuovo: "))

# Messaggio di congratulazioni
print("Congratulazioni! Hai indovinato il numero segreto!")

