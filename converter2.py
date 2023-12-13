import csv
import sys

# Aumenta o limite do tamanho do campo (ajuste conforme necessário)
csv.field_size_limit(sys.maxsize)

# Nome do arquivo de entrada e saída
arquivo_entrada = 'teste.csv'
arquivo_saida = 'novo_arquivo.csv'

# Lista para armazenar as quatro primeiras colunas
colunas_selecionadas = []

# Lê o arquivo de entrada e armazena as quatro primeiras colunas na lista
with open(arquivo_entrada, 'r') as entrada_csv:
    leitor_csv = csv.reader(entrada_csv)
    for linha in leitor_csv:
        # Adiciona as quatro primeiras colunas
        colunas_selecionadas.append(linha[:4])

# Escreve as quatro primeiras colunas no novo arquivo CSV
with open(arquivo_saida, 'w', newline='') as saida_csv:
    escritor_csv = csv.writer(saida_csv)
    escritor_csv.writerows(colunas_selecionadas)

print(f'O novo arquivo "{arquivo_saida}" foi gerado com sucesso!')