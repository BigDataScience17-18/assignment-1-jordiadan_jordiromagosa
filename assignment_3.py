import pandas as pd


def get_column_match_string(data, column, string):
    return data[data[column].str.contains(string)]


data = pd.read_csv("budgets/Pressupostos_dels_ens_municipals_de_Catalunya.csv")

data = get_column_match_string(data, "NOM_COMPLERT", "Ajuntament")


print(data)
