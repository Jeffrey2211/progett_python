user = ""

while user != "chupacabra":
    user = input("Inserisci una parola fino a quando non indovini la parola segreta: ")
    if user == "chupacabra":
        print("Hai abbandonato con successo il loop.")
        break
    else:
        print("Hai sbagliato, ritenta!")