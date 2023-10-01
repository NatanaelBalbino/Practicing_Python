# Resolver as bibliotecas com funções
import string
from unidecode import unidecode

print("Valida Palíndromo")
print("-" * 50)

palavra_original = input("Informe: ")
palavra_semEspacos = palavra_original.replace(' ', '')

# Remover os Acentos
palavra_semAcentuacao = unidecode(palavra_semEspacos)

# Remove as Pontuaçoes
palavra_semAcentuacao = palavra_semAcentuacao.translate(str.maketrans('', '', string.punctuation))

palavra_virada = palavra_semAcentuacao[::-1]

if palavra_virada == palavra_semAcentuacao:
    print(f'"{palavra_original}" é um palíndromo!')
else:
    print(f'"{palavra_original}" não é um palíndromo!')