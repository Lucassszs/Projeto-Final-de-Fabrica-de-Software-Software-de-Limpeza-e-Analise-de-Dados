import pandas as pd
import os

def limpar_e_gerar_planilha(caminho_arquivo, novo_nome_base=None):
    try:
        # Detecta o tipo de arquivo com base na extensão
        extensao = os.path.splitext(caminho_arquivo)[1].lower()

        # Lê a planilha com a função apropriada
        if extensao == '.csv':
            df = pd.read_csv(caminho_arquivo, encoding='latin1')
        elif extensao in ['.xls', '.xlsx']:
            df = pd.read_excel(caminho_arquivo)
        else:
            raise ValueError("Tipo de arquivo não suportado. Use CSV, XLS ou XLSX.")

        # Remove colunas que têm nomes "Unnamed"
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

        # Identifica as colunas principais (as duas primeiras colunas, por exemplo)
        colunas_principais = df.columns[:2].tolist()

        # Remove linhas onde todas as colunas têm valores NaN
        df_limpo = df.dropna(how='all')

        # Registra as alterações
        linhas_removidas = len(df) - len(df_limpo)
        colunas_removidas = [col for col in df.columns if col not in df_limpo.columns]
        colunas_restantes = df_limpo.columns.tolist()

        # Simplifica o nome do arquivo original
        nome_arquivo = os.path.splitext(os.path.basename(caminho_arquivo))[0]

        # Usa o novo nome base se fornecido, caso contrário, usa o nome original simplificado
        nome_base = novo_nome_base if novo_nome_base else nome_arquivo

        # Adiciona a extensão correta ao novo nome de arquivo
        novo_nome = f"{nome_base}-{'_'.join(colunas_principais)}{extensao}"
        
        # Gera o caminho completo para o novo arquivo na pasta "tabelas_limpas"
        caminho_novo_arquivo = os.path.join('data', 'tabelas_limpas', novo_nome)

        # Salva a nova planilha
        if extensao == '.csv':
            df_limpo.to_csv(caminho_novo_arquivo, index=False)
        else:
            df_limpo.to_excel(caminho_novo_arquivo, index=False)

        # Mostra as alterações feitas
        print(f"Nova planilha salva como {caminho_novo_arquivo}")
        print(f"Linhas removidas: {linhas_removidas}")
        print(f"Colunas removidas: {colunas_removidas}")
        print(f"Colunas restantes: {colunas_restantes}")
    
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")
        
# Exemplo de uso
#caminho_arquivo = r'data/arquivos_Brutos/2010-2016-licitacoes.csv'  #Caminho atualizado
#novo_nome_base = None


#chamar função para limpar e gerar planilhas
#limpar_e_gerar_planilha(caminho_arquivo, novo_nome_base)
        