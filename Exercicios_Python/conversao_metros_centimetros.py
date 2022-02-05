#Desenvolva um programa que leia  um valor em metros e o exiba convertido em centímetros e milímetros.
print(('Converta metros em centímetros e milímetros'))
metros = int(input('Digite o valor em metros:'))
centimetros = metros * 100
milimetros = metros *1000
print('{}m para centímetros: {}cm\n{}m para milímetros: {}mm.'.format(metros,centimetros,metros,milimetros))