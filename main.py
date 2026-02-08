# Pedindo a frase ao usuário
frase = input("Digite uma frase: ").lower()

# Definindo o que é uma vogal
vogais = "aeiouáéíóúâêîôûãõ"
contador = 0

# Verificando cada letra
for letra in frase:
    if letra in vogais:
        contador += 1

# Exibindo o resultado
print(f"A frase digitada contém {contador} vogais.")
