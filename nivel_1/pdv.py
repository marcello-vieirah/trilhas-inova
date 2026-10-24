lista_compras = []
total_bruto = 0
qtd_descontos = 0

while True:
    print("\n-=-=-=-=-=--=- Digite 0 para encerrar -=-=-=-=-=--=-")
    valor_compra = float(input("Valor da compra: "))

    if valor_compra == 0:
        break

    if valor_compra < 0:
        print("Aviso: O valor não pode ser negativo.")
        continue

    idade_cliente = int(input("Idade do cliente: "))

    if idade_cliente < 0:
        print("Aviso: A idade não pode ser negativa.")
        continue

    qtd_itens = int(input("Quantidade de itens: "))

    if qtd_itens < 0:
        print("Aviso: A quantidade não pode ser negativa.")
        continue

    cupom = input("Cupom de fidelidade (Enter para ignorar): ")

    total_bruto += valor_compra
    valor_original = valor_compra

    print()
    if idade_cliente >= 65:
        valor_compra *= 0.80
        qtd_descontos += 1
        print(f"desconto de 20% aplicado.")

    if valor_compra > 100:
        valor_compra *= 0.90
        qtd_descontos += 1
        print(f"desconto de 10% aplicado.")

    if qtd_itens > 3:
        valor_compra *= 0.95
        qtd_descontos += 1
        print(f"desconto de 5% aplicado.")

    if cupom == "FIDELIDADE10":
        valor_compra *= 0.90
        qtd_descontos += 1
        print(f"desconto de fidelidade de 10% aplicado.")

    lista_compras.append(valor_compra)

print("\n\n")
print("-" * 30)
print("RESUMO DO DIA")

total_final = sum(lista_compras)
valor_desconto = total_bruto - total_final

print(f"Quantidade de compras: {len(lista_compras)}")
print(f"Total bruto: R$ {total_bruto:,.2f}")
print(f"Descontos concedidos: (qtd) {qtd_descontos} | (R$) {valor_desconto:,.2f}")
print(f"Total final: R$ {total_final:,.2f}")

with open("resumo.txt", "w", encoding="utf-8") as file:
    file.write("HISTÓRICO DE COMPRAS\n\n")

    for i, compra in enumerate(lista_compras, start=1):
        file.write(f"Compra {i}: R$ {compra:.2f}\n")

    file.write("\nRESUMO DO DIA\n\n")
    file.write(f"Quantidade de compras: {len(lista_compras)}\n")
    file.write(f"Total bruto: R$ {total_bruto:,.2f}\n")
    file.write(
        f"Descontos concedidos: (qtd) {qtd_descontos} | "
        f"(R$) {valor_desconto:,.2f}\n"
    )
    file.write(f"Total final: R$ {total_final:,.2f}\n")

print("\nResultados salvos em 'resumo.txt'.")
