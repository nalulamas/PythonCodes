#Leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.
print('Descubra quanto ficará seu salário com 15% de aumento!')
salario =float(input('Digite aqui seu salário:'))
calculo_aumento =0.15*salario
aumento_salario = salario+calculo_aumento
print('Seu sálario de R${} com 15% de aumento é de R${}'.format(salario,aumento_salario))