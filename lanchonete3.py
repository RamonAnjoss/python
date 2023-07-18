print("    Bem-vindos a lanchonete do SENAI!   ")
print("             CARDÁPIO!                  ")
print("CÓDIGO|      DESCRIÇÃO      |VALOR (R$)|")
print(" 100  |   Cachorro quente   |  R$9,00  |")
print(" 101  |Cachorro quente duplo|  R$11,00 |")
print(" 102  |        X-Egg        |  R$12,00 |")
print(" 103  |       X-Salada      |  R$12,00 |")
print(" 104  |       X-Bacon       |  R$14,00 |")
print(" 105  |       X-Tudo        |  R$17,00 |")
print(" 200  | Refrigerante gelado |  R$5,00  |")


cantina = { 100: {"Produto":"Cachorro-quente", "preço": 9.00},
            101: {"Produto":"Cachorro qunete-duplo", "preço": 11.00},
            102: {"Produto":"X_egg", "preço": 12.00},
            103: {"Produto":"X_Salada", "preço": 12.00},
            104: {"Produto":"X_bacon", "preço": 14.00},
            105: {"Produto":"X_tudo", "preço": 17.00},
            200: {"Produto":"Refrigerante Gelado", "preço": 5.00}}

total = 0

def adicionarItem():
    pedido = int(input("Digite o código do Produto: "))
    while pedido not in cantina:
        print('Opção invalida')
        pedido = int(input("Digite novamente o código do produto: "))

    print(f"Você pediu: {cantina[pedido]['produto']}")
    print(f'Preço: {cantina[pedido]["preco"]}')
    return cantina[pedido]["preco"]

total += adicionarItem()

resposta = input('Deseja pedir algo mais? (S/N)').lower()
while resposta == 's' or resposta == 'sim':
    total += adicionarItem()
    resposta = input('Deseja pedir algo mais? (S/N)').lower()

print(f'Total do pedido: R${total:.2f}')

