# Define the dictionary with corrected structure
Pagella = {
    "Giuseppe Giulio": [("Matematica", "voto", 9, "assenze", 0), 
                        ("Italiano", "voto", 7, "assenze", 3),
                        ("Inglese", "voto", 7.5, "assenze", 4), 
                        ("Storia", "voto", 7.5, "assenze", 4),
                        ("Geografia", "voto", 5, "assenze", 7)],
    "Antonio Barbera": [("Matematica", "voto", 8, "assenze", 1), 
                        ("Italiano", "voto", 6, "assenze", 1),
                        ("Inglese", "voto", 9.5, "assenze", 0), 
                        ("Storia", "voto", 8, "assenze", 2),
                        ("Geografia", "voto", 8, "assenze", 1)],
    "Emiliano Ruozzo": [("Matematica", "voto", 7.5, "assenze", 2), 
                        ("Italiano", "voto", 6, "assenze", 2),
                        ("Inglese", "voto", 4, "assenze", 3), 
                        ("Storia", "voto", 8.5, "assenze", 2),
                        ("Geografia", "voto", 8, "assenze", 2)]
}

# Add a new student
Pagella["Albert Einstein"] = [("Matematica", "voto", 10, "assenze", 0), 
                              ("Italiano", "voto", 10, "assenze", 0),
                              ("Inglese", "voto", 10, "assenze", 0), 
                              ("Storia", "voto", 10, "assenze", 0),
                              ("Geografia", "voto", 10, "assenze", 0)]

# Add "Fisica" subject to each student
Pagella["Giuseppe Giulio"].append(("Fisica", "voto", 9.5, "assenze", 0))
Pagella["Antonio Barbera"].append(("Fisica", "voto", 8, "assenze", 1))
Pagella["Emiliano Ruozzo"].append(("Fisica", "voto", 8, "assenze", 3))
Pagella["Albert Einstein"].append(("Fisica", "voto", 10, "assenze", 0))

# Display specific elements
print(Pagella["Giuseppe Giulio"][0])     # Output: ('Matematica', 'voto', 9, 'assenze', 0)
print(Pagella["Emiliano Ruozzo"][2])     # Output: ('Inglese', 'voto', 4, 'assenze', 3)
print(Pagella["Antonio Barbera"][4][2])  # Output: 8

# Display the entire dictionary
print(Pagella)


