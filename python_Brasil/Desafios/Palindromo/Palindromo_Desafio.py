# Resolver as bibliotecas com funções
import string
from unidecode import unidecode

print("Valida Palíndromo")
print("-" * 50)

palavra_original = input("Informe: ")
palavra_semEspacos = palavra_original.replace(' ', '')

# Remover os Acentos e converte para lower case
palavra_semAcentuacao = unidecode(palavra_semEspacos).lower()

# Remove as Pontuaçoes
palavra_semPontuacao = palavra_semAcentuacao.translate(str.maketrans('', '', string.punctuation))

palavra_virada = palavra_semPontuacao[::-1]

if palavra_virada == palavra_semPontuacao:
    print(f'"{palavra_original}" é um palíndromo!')
else:
    print(f'"{palavra_original}" não é um palíndromo!')
