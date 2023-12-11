from langchain.document_loaders import UnstructuredFileLoader
from tinydb import TinyDB, Query
import re
import os



def inf_filename():
    PASTA_ARQUIVOS = "/hdvm12/user/000020/bd/ACT-A_full/"
    lista_arquivos = [arquivo for arquivo in os.listdir(PASTA_ARQUIVOS) if os.path.isfile(os.path.join(PASTA_ARQUIVOS, arquivo))]
    # print(lista_arquivos)

    for arquivo in lista_arquivos:
        full_path_arq = os.path.join(PASTA_ARQUIVOS,arquivo)
        print(full_path_arq)
        categoria = categoria1(arquivo)
        data = data1(arquivo)
        titulo = titulo1(arquivo)
        paragrafos = extrair_pdf(full_path_arq)
        inserir_bd(data=data, categoria=categoria,titulo=titulo,nome_arquivo=arquivo, paragrafos=paragrafos)

def titulo1(string):
    titulo = string.split("_")
    return titulo[-1]
    
        
        
def categoria1(string):
    lista = string.split("_")
    # print(lista)
    for string in lista:
        if not string.isdigit():
            return string

def data1(string):
    strings_numericas = []
    contador = 0

    lista = string.split("_")
    

    for elemento in lista:
        if elemento.isdigit():
            strings_numericas.append(elemento)
            contador += 1
            if contador == 3:
                break  # Interrompe após encontrar três strings numéricas
    
    lista = strings_numericas
    ano = next((item for item in lista if item.isdigit()), '0000')
    mes = next((item for item in lista[1:] if item.isdigit()), '00')
    dia = next((item for item in lista[2:] if item.isdigit()), '00')

    return f"{dia}/{mes}/{ano}"

    

    
def inserir_bd(data="NA", categoria="NA", titulo="NA",nome_arquivo="NA",paragrafos="NA"):
    db = TinyDB(f'teste.json', indent=4, ensure_ascii=False)
    db.insert({
                "data":data,
                "categoria": categoria,
                "titulo":titulo,
                "nome_arquivo": nome_arquivo,
                "paragrafos": paragrafos
            })


def extrair_pdf(pdf_file):
    
    loader = UnstructuredFileLoader(pdf_file)
    documents = loader.load()
  
    # pdf_pages_content = '\n'.join(doc.page_content.split('\n') for doc in documents)
    for doc in documents:
        paragrafos = doc.page_content.split('\n')

    return paragrafos
    


def main():
    DIR = "/hdvm12/user/000020/bd/ACT-A/"
    FILE = "2020_08_06_Showcase_COVAX.pdf"
    text_with_langchain_files = extract_text_with_langchain_pdf(DIR + FILE)
    print(text_with_langchain_files)

if __name__ == '__main__':
    inf_filename()