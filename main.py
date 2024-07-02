from limpeza_de_dados import limpar_e_gerar_planilha

def main():
    # Definir caminho dos arquivos de dados
    caminho_arquivo = r'data/arquivos_Brutos/2010-2016-licitacoes.csv'
    novo_nome_base = None
    
    # Chama a função de limpeza e geração de planilha
    limpar_e_gerar_planilha(caminho_arquivo, novo_nome_base)
    
    # Adicionar outras funções de análise e coleta de dados aqui
    
    print("Processamento concluído.")

if __name__ == "__main__":
    main()
