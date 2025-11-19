import pandas as pd

df_aviao = pd.read_csv("Airplane.csv", sep=",", encoding="utf-8")

# Exibe dados completos
print("=== Dados completos da tabela ===")
print(df_aviao)

# Exibe apenas as primeiras linhas
print("\n=== Primeiras linhas usando head() ===")
print(df_aviao.head())



df_modelo = pd.read_csv("modelos.csv", sep=";", encoding="utf-8")

# Exibe apenas as colunas
print("\nColunas encontradas no arquivo de modelos:")
print(list(df_modelo.columns))

# Exibe os dados atuais
print("\nDados atuais do arquivo modelos.csv:")
print(df_modelo)


# Adicionando novos modelos (atividade 2)


novos_modelos = [
    {"modelo": "Airbus A321neo", "capacidade_media": "185–240", "companhia": "Azul", "ano_fabricacao": 2021},
    {"modelo": "Boeing 747-8 Intercontinental", "capacidade_media": "410–467", "companhia": "Lufthansa", "ano_fabricacao": 2016},
    {"modelo": "Embraer E195-E2", "capacidade_media": "132", "companhia": "KLM", "ano_fabricacao": 2020}
]

df_modelo = pd.concat([df_modelo, pd.DataFrame(novos_modelos)], ignore_index=True)

# Salva no CSV
df_modelo.to_csv("modelos.csv", index=False, sep=";")

print("\nModelo(s) adicionado(s) com sucesso!")


print("\n=== Dados finais do arquivo modelos.csv ===")
print(df_modelo)
