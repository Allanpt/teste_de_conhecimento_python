# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy

from dados.produtos_1 import produtos
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
copia_produtos = copy.deepcopy(produtos)

novos_produtos_mais_10percent = [
    {**produto, 'preco': round(produto.get('preco') * 1.1, 2) }
    for produto in copia_produtos
]

produtos_ordenados_por_nome = sorted(copia_produtos, key=lambda p: p['nome'], reverse=True)

produtos_ordenados_por_preco = sorted(copia_produtos, key=lambda p: p['preco'], reverse=True)

print("Produtos com acréscimo de 10%")
print()
print(*novos_produtos_mais_10percent, sep='\n')
print()
print("Produtos ordenados por nome decrescente")
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print("Produtos ordenados por preço decrescente")
print()
print(*produtos_ordenados_por_preco, sep='\n')
