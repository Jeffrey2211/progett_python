# Input dell'ora di inizio e la durata in minuti
hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Calcolo dell'ora di fine
# Convertiamo l'ora di inizio in minuti totali
minuti_totali_inizio = hour * 60 + mins

# Calcoliamo i minuti totali di fine sommando la durata
minuti_totali_fine = minuti_totali_inizio + dura

# Calcoliamo l'ora di fine e i minuti
ora_fine = minuti_totali_fine // 60  # Divisione intera per ottenere le ore
minuti_fine = minuti_totali_fine % 60  # Resto della divisione per ottenere i minuti

# Stampiamo il risultato nel formato richiesto
print("L'evento inizia alle " + str(hour) + "," + str(mins) + " e termina alle " + str(ora_fine) + "," + str(minuti_fine))
