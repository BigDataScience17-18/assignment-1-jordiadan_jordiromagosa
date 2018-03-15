import pandas as pd
import numpy as np


def get_column_match_string(data, column, string):
    return data[data[column].str.contains(string)]


def get_town_councils():
    data = pd.read_csv("budgets/Pressupostos_dels_ens_municipals_de_Catalunya.csv")

    data = get_column_match_string(data, "NOM_COMPLERT", "Ajuntament")
    return data.loc[data["IMPORT"] > 0]


def level_expenses(data):
    levels = np.unique(data.NIVELL)
    expenses = []
    for i in levels:
        current = data.loc[data["NIVELL"] == i]
        expenses.append(current["IMPORT"].sum())
    return expenses


def get_town_council_entry_num(data):
    name, counts = np.unique(data.NOM_COMPLERT, return_counts=True)
    return dict(zip(name, counts))


town_councils = get_town_councils()

print(level_expenses(town_councils))
