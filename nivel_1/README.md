# PDV com Descontos

## O que o código faz

Este projeto implementa um sistema simples de **Ponto de Venda (PDV)** em Python. Ele recebe os dados de cada compra e **aplica descontos** de acordo com a `idade do cliente`, `valor da compra`, `quantidade de itens` e um possível `cupom de fidelidade`.

Ao final, apresenta um **resumo financeiro** e **salva** o histórico em um arquivo `resumo.txt`

## Como funciona

O programa solicita várias informações ao usuário, e caso o mesmo digite 0 no campo `valor da compra`, o programa é **encerrado** exibindo o resumo do dia.

**Observação: São rejeitados números negativos em campos não permitidos.**

Os descontos são aplicados da seguinte forma:

1. `idade do cliente` >= 65 anos: recebe 20% de desconto;
2. `valor da compra` > R$ 100,00 (mesmo após desconto por idade): recebe 10% de desconto;
3. `quantidade de itens` > 3: recebe 5% de desconto;
4. `cupom de fidelidade` FIDELIDADE10 informado: recebe 10% de desconto.

O valor final de cada compra é armazenado em uma lista utilizando `.append()`, e ao encerrar, o programa calcula a `quantidade de compras`, o `total bruto`, o `total de descontos concedidos` e o `total final`.

O resumo e o histórico das compras são exibidos no **console** e **gravados** no arquivo `resumo.txt`, utilizando `open()` e um loop `for`.

**Observação: os descontos são aplicados sequencialmente sobre o valor atualizado da compra.**

## Tabela de casos de teste

| Valor da compra | Idade | Desconto idade | Desconto valor | Valor final esperado |
|---:|---:|---:|---:|---:|
| R$ 50,00 | 30 | 0% | 0% | R$ 50,00 |
| R$ 100,00 | 30 | 0% | 0% | R$ 100,00 |
| R$ 80,00 | 65 | 20% | 0% | R$ 64,00 |
| R$ 100,00 | 70 | 20% | 0% | R$ 80,00 |
| R$ 125,00 | 70 | 20% | 0% | R$ 100,00 |
| R$ 200,00 | 30 | 0% | 10% | R$ 180,00 |
| R$ 101,00 | 30 | 0% | 10% | R$ 90,90 |
| R$ 200,00 | 65 | 20% | 10% | R$ 144,00 |
| R$ 1000,00 | 80 | 20% | 10% | R$ 720,00 |
| R$ 200,00 | 64 | 0% | 10% | R$ 180,00 |

## Como executar

No terminal, entre na pasta `nivel_1` e execute o arquivo `pdv.py`:

```bash
python pdv.py
```
O programa solicitará os dados de cada compra até que o valor 0 seja informado.
