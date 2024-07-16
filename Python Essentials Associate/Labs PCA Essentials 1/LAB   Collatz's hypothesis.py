c0 = int(input("Inserisci un numero intero non negativo diverso da zero: "))

if c0 <= 0:
    print("Il numero deve essere maggiore di zero.")
else:
    steps = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
        print(c0)
        steps += 1

    print("Numero di passaggi:", steps)

