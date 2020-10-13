# Os colchetes ([]) indicam uma lista e os elementos individuais da lista são separados por vírgulas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles)

# Acessando elementos em uma lista:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0])

# Podemos formatar o elemento 'trek' de maneira mais organizada usando o método title() :

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

# Python possui uma sintaxe especial para acessar o último elemento em uma list. Ao solicitar o item no índice -1,
# o Python retorna sempre o último item da list:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

# Usando valores individuais de uma list:

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
message = f"My first bicycle was a {bicycles[0].title()}."

print(message)
