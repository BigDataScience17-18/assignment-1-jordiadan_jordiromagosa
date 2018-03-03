import pandas as pd
import os

trainAlcoholic = [
    364,    365,    368,    369,    370,    371,    372,    375,    377,    378
]

trainNonAlcoholic = [
    337,    338,    339,    340,    341,    342,    344,    345,    346,    347
]

testAlcoholic = [
    379,    380,    381,    382,    384,    385,    386,    387,    388,    390
]

testNonAlcoholic = [
    348,    351,    352,    354,    355,    356,    357,    359,    362,    363
]


def get_column_names():
    column_names = ["Id", "Alcoholic", "Paradigm", "Replication", "Channel"]
    for reading in range(256):
        column_names.append("Reading " + str(reading+1))
    return column_names


def read_file(user_id, alcoholic):
    file_name = "results/co2"
    if alcoholic:
        file_name += "a"
    else:
        file_name += "c"
    if user_id > 1000:
        user_id -= 1000
    file_name += "0000" + str(user_id) + ".txt"
    file_data = pd.read_csv(file_name, sep=" ", header=None, names=get_column_names())
    return file_data.drop_duplicates()


def read_all_users(users, alcoholic):
    all_users = read_file(users[0], alcoholic)
    for user in range(1, len(users)):
        temp_users = all_users.append(read_file(users[user], alcoholic))
        all_users = temp_users
    return all_users


def get_train_alcoholic():
    return read_all_users(trainAlcoholic, True)


def get_train_non_alcoholic():
    return read_all_users(trainNonAlcoholic, False)


def get_test_alcoholic():
    return read_all_users(testAlcoholic, True)


def get_test_non_alcoholic():
    return read_all_users(testNonAlcoholic, False)


def feature_engineering_row(data):
    reading_columns = []
    for reading in range(256):
        reading_columns.append("Reading " + str(reading + 1))
    processed_data = data.copy()
    processed_data["Min"] = processed_data[reading_columns].min(axis=1)
    processed_data["Max"] = processed_data[reading_columns].max(axis=1)
    processed_data["Std"] = processed_data[reading_columns].std(axis=1)
    processed_data["Mean"] = processed_data[reading_columns].mean(axis=1)
    processed_data["Median"] = processed_data[reading_columns].median(axis=1)
    processed_data["Quantile025"] = processed_data[reading_columns].quantile(0.025, axis=1)
    processed_data["Quantile25"] = processed_data[reading_columns].quantile(0.25, axis=1)
    processed_data["Quantile75"] = processed_data[reading_columns].quantile(0.75, axis=1)
    processed_data["Quantile975"] = processed_data[reading_columns].quantile(0.975, axis=1)
    processed_data["IQR"] = processed_data["Quantile75"] - processed_data["Quantile25"]

    return processed_data.drop(columns=reading_columns)


def feature_engineering_column(data):
    reading_columns = []
    for reading in range(256):
        reading_columns.append("Reading " + str(reading + 1))
    mean_table = data.groupby(["Id", "Alcoholic", "Paradigm", "Channel"])[reading_columns].mean()

    return mean_table.reset_index()


def create_and_get_path_engineering(identification_path):
    if not os.path.exists("engineered"):
        os.makedirs("engineered")
    return "engineered/" + identification_path + ".csv"


def user_feature_engineering_and_save(user_id, alcoholic, columns, identification_path):
    data = read_file(user_id, alcoholic)
    if columns:
        data = feature_engineering_column(data)
        identification_path += "_columns"
    else:
        data = feature_engineering_row(data)
        identification_path += "_rows"
    path = create_and_get_path_engineering(identification_path)
    data.to_csv(path, header=False, index=False, mode="a")


def process_all_users_feature_engineering(user_ids, alcoholic, identification_path):
    for user in user_ids:
        user_feature_engineering_and_save(user, alcoholic, True, identification_path)
        user_feature_engineering_and_save(user, alcoholic, False, identification_path)


process_all_users_feature_engineering(trainAlcoholic, True, "train_alcoholic")
process_all_users_feature_engineering(trainNonAlcoholic, False, "train_non_alcoholic")
process_all_users_feature_engineering(testAlcoholic, True, "test_alcoholic")
process_all_users_feature_engineering(testNonAlcoholic, False, "test_non_alcoholic")