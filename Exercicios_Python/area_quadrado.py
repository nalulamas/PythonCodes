#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#A = b.h ou A = L²
print('Descubra a area de um quadrado.')
largura_quadrado = int(input('Digite a largura:'))
altura_quadrado = int(input('Digite a altura:'))
area_quadrado = largura_quadrado * altura_quadrado
area_dobro_quadrado = area_quadrado *2
print('A area do quadrado é igual a: {} e seu dobro equivale a {}'.format(area_quadrado,area_dobro_quadrado))