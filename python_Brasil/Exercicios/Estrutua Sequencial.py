#1. Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('ex1')
print('Alo mundo')
print('-'*50)
#2. Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
print('ex2')
ex2 = input('Informe um número')
print(ex2)
print('-'*50)
#3. Faça um Programa que peça dois números e imprima a soma.
print('ex3')
ex3_n1 = eval(input('informe o primeiro numero:'))
ex3_n2 = eval(input('informe o segundo número:'))
ex3_result = ex3_n1 + ex3_n2
print(f'A soma desses números é {ex3_result}')
print('-'*50)
#4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
print('ex4')
ex4_n1 = eval(input('Informe a primeira nota:'))
ex4_n2 = eval(input('Informe a segunda nota:'))
ex4_n3 = eval(input('Informe a terceira nota:'))
ex4_n4 = eval(input('Informe a quarta nota:'))
ex4_media = (ex4_n1 + ex4_n2 + ex4_n3 + ex4_n4) / 4
print(f'A média das suas notas é {ex4_media}')
print('-'*50)
#5. Faça um Programa que converta metros para centímetros.
print('ex5')
ex4_metros = eval(input('Informe os metros e converterei para centimetros'))
ex4_centimetros = ex4_metros * 100
print(f'{ex4_metros} metros são {ex4_centimetros} centimetros')
print('-'*50)
#6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
print('ex6')
    #Formula para area do circulo A = πr^2
ex6_raio = eval(input(('Informe o raio para que eu calcule a área:')))
c_PI = 3.14
ex6_area = c_PI * (ex6_raio**2)
print(f'O valor da area do circulo é de {ex6_area}')
print('-'*50)
#7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
print('ex7')
    #Formula  para area do quadrado A = L * L ou L^2 (sendo L o o valor da lateral do quadrado)
ex7_lateral = eval(input('Informe o valor lateral do quadrado para que eu lhe retorne o dobro da área:'))
ex7_area = ex7_lateral**2
print(f'O dobro do valor da area do quadrado é de {ex7_area * 2}')
print('-'*50)
#8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
print('ex8')
ex8_valorHora = eval(input('Informe o seu valor hora trabalhado:'))
ex8_horaTrabalhada = eval(input('Informe o número de horas trabalhadas:'))
ex8_salario = ex8_horaTrabalhada * ex8_valorHora
print(f'O Valor a ser pago é de {ex8_salario}')
print('-'*50)
#9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
    #C = 5 * ((F-32) / 9).
print('ex9')
ex9_fahrenheit = eval(input('Informe o valor em Fahrenheit e transformarei em Celsius:'))
ex9_celsius = 5 *((ex9_fahrenheit-32)/9)
print(f'A conversão deu em {ex9_celsius}ºC')
print('-'*50)
#10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
    #(0 °C × 9/5) + 32 = 32 °F
print('ex10')
ex10_celsius = eval(input('Informe o valor em Graus Celsius e transformarei para Graus Fahrenheit:'))
ex10_fahrenheit = (ex10_celsius * (9 / 5)) + 32
print(f'A conversão deu em {ex10_fahrenheit}ºF')
print('-'*50)
#11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
    #o produto do dobro do primeiro com metade do segundo.
    #a soma do triplo do primeiro com o terceiro.
    #o terceiro elevado ao cubo.

#12. Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
#13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:

    #Para homens: (72.7*h) - 58
    #Para mulheres: (62.1*h) - 44.7

#14. João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.
#15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

    #salário bruto.
    #quanto pagou ao INSS.
    #quanto pagou ao sindicato.
    #o salário líquido.
    #calcule os descontos e o salário líquido, conforme a tabela abaixo:

    #+ Salário Bruto : R$
    #- IR (11%) : R$
    #- INSS (8%) : R$
    #- Sindicato ( 5%) : R$
    #= Salário Liquido : R$

    #Obs.: Salário Bruto - Descontos = Salário Líquido.

#16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
#17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

    #Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    #comprar apenas latas de 18 litros;
    #comprar apenas galões de 3,6 litros;
    #misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

#18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).