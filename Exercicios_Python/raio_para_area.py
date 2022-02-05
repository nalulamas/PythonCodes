#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# A = 3,14 * r²
print('Descubra a area de um circulo através do raio')
raio =float(input('Raio:'))
raio_dobro =raio ** 2
area =float(3.14 * raio_dobro)
print('A area do raio {} é igual a {}'.format(raio, area))