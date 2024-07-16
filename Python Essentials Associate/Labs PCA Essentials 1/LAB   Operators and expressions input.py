x = float(input("Inserire il valore di x: "))

# Calcolo delle espressioni intermedie
# Calcoliamo la parte più interna dell'espressione: 1 / x
inner_most = 1 / x

# Aggiungiamo x alla parte calcolata sopra: x + (1 / x)
third_inner = x + inner_most

# Calcoliamo la nuova espressione interna: 1 / (x + (1 / x))
second_inner = 1 / third_inner

# Aggiungiamo x alla parte calcolata sopra: x + (1 / (x + (1 / x)))
first_inner = x + second_inner

# Calcoliamo la nuova espressione interna: 1 / (x + (1 / (x + (1 / x))))
innermost_expression = 1 / first_inner

# Infine, calcoliamo il valore di y: 1 / (1 + (1 / (x + (1 / (x + (1 / x))))))
y = 1 / (1 + innermost_expression)

# Stampa del risultato
print("y =", y)

