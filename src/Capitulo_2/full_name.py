# Uso de variáveis em Strings

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# Podemos usar f-strings para escrever mensagens completas usando as informações associadas a uma variável

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

# Podemos usar f-strings para mostrar uma mensagem e, em seguida, atribuir essa mensagem a uma variável

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)
