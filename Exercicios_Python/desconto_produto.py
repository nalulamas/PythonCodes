#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto
print('Estamos com 5% de desconto em nossos produtos!')
valor_produto =float(input('Digite o valor do produto aqui para calcularmos o desconto:'))
calculo_desconto = (0.05*valor_produto)
desconto_produto = valor_produto - calculo_desconto
print('O valor de {} com 5% de desconto é de {}'.format(valor_produto,desconto_produto))