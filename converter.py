import csv
from tinydb import TinyDB

# Caminho para o arquivo TinyDB
tinydb_path = '/home/lantri_rafaelalmeida/codigo/diss/teste.json'

# Caminho para o arquivo CSV de saída
csv_path = '/home/lantri_rafaelalmeida/codigo/diss/teste.csv'

# Inicializa o objeto TinyDB
db = TinyDB(tinydb_path)

# Obtém todos os registros da tabela padrão (default)
registros = db.all()

# Fecha o banco de dados
db.close()

# Abre o arquivo CSV para escrita
with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
    # Cria um objeto de escrita CSV
    csv_writer = csv.writer(csv_file)

    # Escreve o cabeçalho (nomes das colunas)
    if registros:
        cabecalho = registros[0].keys()
        csv_writer.writerow(cabecalho)

        # Escreve os dados
        for registro in registros:
            csv_writer.writerow(registro.values())

print(f'Dados do TinyDB foram convertidos com sucesso para {csv_path}.')
