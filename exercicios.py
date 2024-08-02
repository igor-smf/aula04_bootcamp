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

# 6. Eliminação de Duplicatas
# Objetivo: Dada uma lista de emails, remover todos os duplicados.

# 7. Filtragem de Dados
# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que 
# são maiores ou iguais a 18.

idades = [22, 15, 30, 17, 18]
idade_validas = [idade for idade in idades if idade >= 18]
print("\n", idade_validas)

# 8. Ordenação Personalizada
# Objetivo: Dada uma lista de dicionários representando pessoas, 
# ordená-las pelo nome.

pessoas = [
    {"nome": "Bob", "idade": 25},
    {"nome": "Alice", "idade": 30},    
    {"nome": "Carol", "idade": 20}
]

print("\n", sorted(pessoas, key=lambda pessoa: pessoa["nome"]))

# 9. Agregação de Dados
# Objetivo: Dado um conjunto de números, calcular a média.

# 10. Divisão de Dados em Grupos
# Objetivo: Dada uma lista de valores, dividir em duas listas: 
# uma para valores pares e outra para ímpares.

# 11. Atualização de Dados
# Objetivo: Dada uma lista de dicionários representando produtos, 
# atualizar o preço de um produto específico.

produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

for p in produtos:
    if p["id"] == 2:
        p["preço"] = 90

print("\n", produtos)

# 12. Fusão de Dicionários
# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

# 13. Filtragem de Dados em Dicionário
# Objetivo: Dado um dicionário de estoque de produtos, 
# filtrar aqueles com quantidade maior que 0.

# 14. Extração de Chaves e Valores
# Objetivo: Dado um dicionário, criar listas separadas para suas 
# chaves e valores.

# 15. Contagem de Frequência de Itens
# Objetivo: Dada uma string, contar a frequência de cada caractere 
# usando um dicionário.

# Funções
# Escreva uma função que receba uma lista de números 
# e retorne a soma de todos os números.


# Crie uma função que receba um número como argumento 
# e retorne True se o número for primo e False caso contrário.

def is_primo(numero):
    if numero > 1:
        for i in range(2, numero):
            if numero % i == 0:
                return False
        return True

print("\n", is_primo(17))

# Desenvolva uma função que receba uma string como argumento 
# e retorne essa string revertida.

# Implemente uma função que receba dois argumentos: uma lista de 
# números e um número. A função deve retornar todas as combinações 
# de pares na lista que somem ao número dado.


# Escreva uma função que receba um dicionário e retorne uma lista 
# de chaves ordenadas