from tinydb import TinyDB, Query

def tratar():
     db = TinyDB(f'teste.json', indent=4, ensure_ascii=False)
     for dado in db:
        paragrafos = dado["paragrafos"]
        nome_arquivo = dado["nome_arquivo"]
        tirar_strings_vazias = [s for s in paragrafos if not (s.strip().isdigit() or s.strip() == "")]
        add_infos = {
            "paragrafos": tirar_strings_vazias
        }
        atualizar_bd(nome_arquivo, add_infos)



def atualizar_bd(nome_arquivo, add_infos):
    db = TinyDB(f'teste.json', indent=4, ensure_ascii=False)
    buscar = Query()
    db.upsert(add_infos, (buscar.nome_arquivo == nome_arquivo))



def main():
    tratar()


if __name__ == '__main__':
    main()