#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessária pra pinta-la,sabendo que cada litro de tinta pinta uma aera de 2m²
#A= b.l
print('Saiba quantas latas de tinta comprar para pintar sua parede! Cada lata rende 2m².')
base= int(input('Digite aqui a base:'))
altura = int(input('Digite aqui a altura:'))
print('Você ira precisar de',(altura*base)/2), 'de lata(s).'