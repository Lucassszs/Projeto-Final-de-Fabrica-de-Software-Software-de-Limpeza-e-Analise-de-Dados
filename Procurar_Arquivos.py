import os
import shutil

def listar_arquivos(pasta):
    arquivos = os.listdir(pasta)
    arquivos_csv_xls = [arquivo for arquivo in arquivos if arquivo.endswith(('.csv', '.xls', '.xlsx'))]
    return arquivos_csv_xls

def escolher_arquivos(arquivos, pasta_arquivos_brutos):
    while True:
        print("\nEscolha os arquivos que deseja processar (separados por vírgula) ou adicione um novo arquivo:")
        for i, arquivo in enumerate(arquivos):
            print(f"{i + 1}. {arquivo}")
        print(f"{len(arquivos) + 1}. Adicionar novo arquivo")

        escolhas = input("Digite os números correspondentes aos arquivos: ")
        indices_escolhidos = [int(x) - 1 for x in escolhas.split(',') if x.strip().isdigit()]

        if len(arquivos) in indices_escolhidos:
            adicionar_arquivo(pasta_arquivos_brutos)
            arquivos = listar_arquivos(pasta_arquivos_brutos)
        else:
            arquivos_escolhidos = [arquivos[i] for i in indices_escolhidos if i >= 0 and i < len(arquivos)]
            if arquivos_escolhidos:
                return arquivos_escolhidos

def adicionar_arquivo(pasta_arquivos_brutos):
    print("\nAdicione o caminho completo do novo arquivo:")
    caminho_novo_arquivo = input("Caminho do novo arquivo: ").strip()
    if os.path.isfile(caminho_novo_arquivo) and caminho_novo_arquivo.endswith(('.csv', '.xls', '.xlsx')):
        shutil.copy(caminho_novo_arquivo, pasta_arquivos_brutos)
        print(f"Arquivo {os.path.basename(caminho_novo_arquivo)} adicionado com sucesso.")
    else:
        print("Arquivo inválido ou não encontrado. Certifique-se de que o caminho e o tipo de arquivo são válidos.")
