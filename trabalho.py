def calcular_conta_recursivo(items, index=0): #função para calcular o valor total da conta, recebe uma lista de itens e um indicie como parametro     

    if index == len(items): #verifica se o indicie é igual ao numero da lista de itens e se for retorna 0 para encerrar
                            #caso o numero for diferente de 0 ele calcula o subtotal do item atual somando a quantidade multiplicada pelo preço
        return 0            #e chama a função recursivamente para o próximo item, aumentando o índice em 1.
    
    quantidade, preco = items[index]
    subtotal = quantidade * preco
    
    return subtotal + calcular_conta_recursivo(items, index+1)

def main():                                        #A função main coleta o número de itens e os detalhes de cada item usando um loop. Depois, 
                                                   #chama a função calcular_conta_recursivo para calcular o valor total da conta usando recursão e imprime o resultado.
    n = int(input("Digite o número de itens: "))
    items = []
    
    for _ in range(n):
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))
        items.append((quantidade, preco))
    
    total = calcular_conta_recursivo(items)
    print(f"Valor total da conta: R${total:.2f}")

if __name__ == "__main__":
    main()
