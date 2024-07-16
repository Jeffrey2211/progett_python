# Step 1
beatles = []
print("Step 1:", beatles)

# Step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3 

for _ in range(2):  # Esegui il loop due volte
    member = input("Inserisci il nome di un membro della band (Stu Sutcliffe, Pete Best): ")
    beatles.append(member)

print("Step 3:", beatles)

# Step 4
del beatles[-2:]  # Rimuove gli ultimi due elementi (Stu Sutcliffe e Pete Best)
print("Step 4:", beatles)

# Step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# Testing della lunghezza della lista
print("The Fab", len(beatles))
