'''Precisamos fazer o controle de classificação de comidas.
   Quando vamos cadastrar uma comida no estoque, ele deve
automaticamente classificar como perecível e não perecível.
   A comida perecível sempre começa com o código "PER"
a comida não perecível com o código ‘PEN’.
   Exemplo de Códigos: PER1235 e PEN9845 '''

#entrada do código do produto
#verificar se código tem 'PER'
#SAÍDA: Caso eu tenha PER no código: TRUE, caso contrário ele me retorna False
#Informar ao usuário True = Perecível e False = Não Perecível

#ENTRADA
codigo = input('Digite o código do produto: ').upper()

print('PER' in codigo)

print('Se a resposta foi TRUE, o produto é perecível')
print('Se a resposta foi FALSE, o produto é não perecível')