def calcular_conta_loop(items):  #função chamada calcular_conta_loop que recebe uma lista de tuplas chamada items como parâmetro.
    total = 0                    # Essa função calcula o valor total da conta somando os subtotais de cada item.
    
    for quantidade, preco in items:
        subtotal = quantidade * preco
        total += subtotal
        
    return total

def main():                                         #onde a execução do programa começa. Ela solicita ao usuário o número de itens e, em seguida, entra em um loop que coleta a quantidade e o preço de cada item e os adiciona à lista items. Depois, 
    n = int(input("Digite o número de itens: "))    #chama a função calcular_conta_loop para calcular o total da conta com base na lista de itens e imprime o valor total formatado.
    items = []
    
    for _ in range(n):
        quantidade = int(input("Digite a quantidade: "))
        preco = float(input("Digite o preço: "))
        items.append((quantidade, preco))
    
    total = calcular_conta_loop(items)
    print(f"Valor total da conta: R${total:.2f}")

if __name__ == "__main__":
    main()
