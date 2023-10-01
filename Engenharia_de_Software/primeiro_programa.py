print("CALCULO de IMC")
print("-"*50)

peso = eval(input('Qual o seu Peso?'))
altura =  eval(input('Qual a sua Altura?'))
IMC = peso / (altura**2)

print (f"O Valor do seu IMC é de {IMC}")