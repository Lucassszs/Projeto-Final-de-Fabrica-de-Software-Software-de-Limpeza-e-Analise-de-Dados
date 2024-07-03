import os
from limpeza_de_dados import limpar_e_gerar_planilha
from Procurar_Arquivos import listar_arquivos, escolher_arquivos

def main():
    pasta_arquivos_brutos = 'data/arquivos_Brutos'
    arquivos = listar_arquivos(pasta_arquivos_brutos)
    
    if not arquivos:
        print("Nenhum arquivo encontrado na pasta.")
    
    arquivos_escolhidos = escolher_arquivos(arquivos, pasta_arquivos_brutos)
    
    if not arquivos_escolhidos:
        print("Nenhum arquivo escolhido.")
        return
    
    for arquivo in arquivos_escolhidos:
        caminho_arquivo = os.path.join(pasta_arquivos_brutos, arquivo)
        novo_nome_base = None
        
        limpar_e_gerar_planilha(caminho_arquivo, novo_nome_base)
    
    print("Processamento concluído.")

if __name__ == "__main__":
    main()
