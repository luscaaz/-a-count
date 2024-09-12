def count_a_in_string(text):
    count = 0
    for char in text:
        if char.lower() == 'a':
            count += 1
    return count

# Usuário digita a frase
user_input = input("Digite uma frase: ")

# Contar 'a' na frase
count_a = count_a_in_string(user_input)

# Exibir o resultado
if count_a > 0:
    print(f"A letra 'a' ocorre {count_a} vez(es) na frase.")
else:
    print("A letra 'a' não foi encontrada na frase.")