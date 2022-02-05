#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
print('Digite um número e mostraremos seu dobro, triplo e sua a raiz quadrada.')
numero = int(input('Digite-o aqui:'))
dobro_numero = numero*2
triplo_numero = numero*3
raiz_numero = int(numero**(1/2))
print('Você digitou {}.\nSeu dobro é {}, o triplo é {} e a sua raiz quadrada vale {}.'. format(numero, dobro_numero,triplo_numero, raiz_numero))