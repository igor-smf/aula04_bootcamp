# Crie uma lista com os números de 1 a 10 
# e use um loop para imprimir cada número elevado ao quadrado.

numeros = [] 
numeros.extend(range(1,11))
numeros_elevado_2 = [numero**2 for numero in numeros]
print("\n",numeros_elevado_2)


# Dada a lista ["Python", "Java", "C++", "JavaScript"], 
# remova o item "C++" e adicione "Ruby".

lista = ["Python", "Java", "C++", "JavaScript"]
lista.remove("C++")
lista.append("Ruby")
print(lista)

# Crie um dicionário para armazenar informações de um livro, 
# incluindo título, autor e ano de publicação. Imprima cada informação.
from typing import Dict, Any

livro: Dict[str, Any] = {
    "Titulo": "Engenharia de dados",
    "Autor": "Luciano",
    "Ano": 2024
}

for chave, valor in livro.items():
    print(chave, valor)

# Escreva um programa que conta o número de ocorrências de cada 
# caractere em uma string usando um dicionário.

def contar_caracteres(string):
    contagem = {}
    for s in string:
        if s in contagem.keys():
            contagem[s] += 1
        else:
            contagem[s] = 1
    return contagem

print(contar_caracteres("engenharia de dados"))


# Dada a lista ["maçã", "banana", "cereja"] e o dicionário 
# {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

lista_compras = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
preço_total = 0

for valor in lista_compras.values():
    preço_total += valor

print(f"O valor total da sua compra é {preço_total}.")