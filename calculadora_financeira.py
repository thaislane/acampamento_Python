''' Crie uma calculadora financeira em que o usuário informa:
   - Faturamento bruto;
   - Taxa de impostos(%)
   - Custos de Operação
 O programa deve devolver o faturamento liquido da empresa'''

#TODO
#ENTRAR: fat_bruto; taxa_imposto; custos
#imposto =
#CÁLCULO: fat_liquido = fat_bruto - imposto - custos
#RETORNAR: fat_liquido

#ENTRADA
fat_bruto = float(input('Entre com o faturamento bruto: '))
taxa_imposto = float(input('Entre com a % da taxa de imposto: '))
custos = float(input('Entre com o custo: '))

#CONTAS
imposto = fat_bruto * taxa_imposto/100
fat_liquido = fat_bruto - imposto - custos

#SAÍDA
print('O faturamento líquido foi de R${:.2f}'.format(fat_liquido))
print('Faturamento bruto R$ {}, Imposto R$ {}, Custo R$ {}, Liquido R$ {}'.format(fat_bruto, imposto, custos, fat_liquido))