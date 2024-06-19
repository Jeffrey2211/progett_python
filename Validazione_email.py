def validate_email(email):
    parts = email.split("@")

    if len(parts) != 2:
        return False

    name, domain_ext = parts

    domain_parts = domain_ext.split(".")

    if len(domain_parts) != 2:
        return False

    domain, ext = domain_parts

    # Verifica che il nome utente contenga solo caratteri validi
    if not name.replace("-", "").replace("_", "").isalnum():
        return False

    # Verifica che il dominio contenga solo caratteri alfanumerici
    if not domain.isalnum():
        return False

    # Verifica che l'estensione del dominio sia composta solo da caratteri alfabetici e di lunghezza massima 3
    if len(ext) > 3 or not ext.isalpha():
        return False

    return True

def filter_emails(emails):
    valid_emails = list(filter(validate_email, emails))
    valid_emails.sort()
    return valid_emails

user_input = input("Inserisci una o più email separate da spazi: ")

# Dividi le email inserite in una lista
emails_to_filter = user_input.split()

# Liste per conservare le email valide e non valide
valid_emails = []
invalid_emails = []

# Ciclo per valutare ciascuna email
for email in emails_to_filter:
    if validate_email(email):
        valid_emails.append(email)
    else:
        invalid_emails.append(email)

# Stampa delle email valide e non valide trovate
print("Email valide trovate:", valid_emails)
print("Email non valide trovate:", invalid_emails)
