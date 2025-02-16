import pandas as pd


def carregar_planilha_caderno_servico(caminho_arquivo):
    df = pd.read_excel(caminho_arquivo)
    return df


def buscar_informacoes(df, nome_servico):
    servico_info = df[df["servico"].str.contains(nome_servico, case=False, na=False)]
    if not servico_info.empty:
        return servico_info.to_dict(orient="records")
    return None
