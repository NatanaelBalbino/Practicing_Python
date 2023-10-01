print('*' * 15, "Valida Palíndromo", '*' * 15)
print("_" * 50)

# Função criada para remover a acentuação, pontuação e conversão da string para lower case
def remove_acentuacao_e_pontuacao(palavra_original):

    palavra_sempontuacao = ''

    # Esse bloco Remove a Pontuação
    for i in palavra_original:
        if i.isalpha() or i.isdigit():
            palavra_sempontuacao += i

    # Esse bloco Remove a Acentuação
    letras_de = 'áéíóúàèìòùâêîôûãõäëïöüçñÿýÁÉÍÓÚÀÈÌÒÙÂÊÎÔÛÃÕÄËÏÖÜÇÑŸÝ'
    letras_para = 'aeiouaeiouaeiouaoaeioucnyyAEIOUAEIOUAEIOUAOAEIOUCNYY'
    palavra_retorno = ''
    contador = 0

    while contador < len(palavra_sempontuacao):

        letra = palavra_sempontuacao[contador]
        contador += 1
        indice = letras_de.find(letra)

        if indice == -1:
            palavra_retorno += letra

        else:
            palavra_retorno += letras_para[indice]
    # Retornando a palavra e convertendo para lower case
    return palavra_retorno.lower()


# Solicitando palavra
palavra_original = input("Informe uma palavra para que eu verifique se a mesma é um palíndromo: ")

# Tratando a palavra com a função criada
palavra_tratada = remove_acentuacao_e_pontuacao(palavra_original)

# Virando a palavra ao contrário
palavra_virada = palavra_tratada[::-1]

# Comparando e imprimindo o resultado
if palavra_virada == palavra_tratada:
    print(f'"{palavra_original}" é um palíndromo!')
else:
    print(f'"{palavra_original}" não é um palíndromo!')