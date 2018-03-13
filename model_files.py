import pandas as pd


def read_file(filename):
    data = pd.read_csv(filename, header=None)
    return data.drop_duplicates()


def write_file(filename, data):
    data.to_csv("model_files/" + filename + ".csv", index=False, mode="w")


def prepare_columns_train():
    data = read_file("engineered/train_alcoholic_columns.csv")
    data = data.append(read_file("engineered/train_non_alcoholic_columns.csv"))

    column_names = ["Id", "Alcoholic", "Paradigm", "Channel"]
    for reading in range(256):
        column_names.append("Reading " + str(reading+1))
    data.columns = column_names
    data["Alcoholic"] = data["Alcoholic"] == "a"

    write_file("train_1_columns", data)


def prepare_rows_train():
    data = read_file("engineered/train_alcoholic_rows.csv")
    data = data.append(read_file("engineered/train_non_alcoholic_rows.csv"))

    column_names = ["Id", "Alcoholic", "Paradigm", "Replication", "Channel", 'Min', 'Max', 'Sd', 'Mean', 'Median', 'IQR', 'Q(0.025)',
                    'Q(0.25)', 'Q(0.75)', 'Q(0.975)']
    data.columns = column_names
    data["Alcoholic"] = data["Alcoholic"] == "a"

    write_file("train_1_rows", data)


def prepare_columns_test():
    data = read_file("engineered/test_alcoholic_columns.csv")
    data = data.append(read_file("engineered/test_non_alcoholic_columns.csv"))

    column_names = ["Id", "Alcoholic", "Paradigm", "Channel"]
    for reading in range(256):
        column_names.append("Reading " + str(reading+1))
    data.columns = column_names
    data["Alcoholic"] = data["Alcoholic"] == "a"

    write_file("test_1_columns", data)


def prepare_rows_test():
    data = read_file("engineered/test_alcoholic_rows.csv")
    data = data.append(read_file("engineered/test_non_alcoholic_rows.csv"))

    column_names = ["Id", "Alcoholic", "Paradigm", "Replication", "Channel", 'Min', 'Max', 'Sd', 'Mean', 'Median', 'IQR', 'Q(0.025)',
                    'Q(0.25)', 'Q(0.75)', 'Q(0.975)']
    data.columns = column_names
    data["Alcoholic"] = data["Alcoholic"] == "a"

    write_file("test_1_rows", data)


#prepare_rows_test()
#prepare_columns_test()
#prepare_rows_train()
#prepare_columns_train()

