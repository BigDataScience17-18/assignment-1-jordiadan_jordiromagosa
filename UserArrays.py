import pandas as pd


trainAlcoholic = [
    385,    1384,   380,    1382,   418,    412,    372,    1396,   1364,   1395,   1381,   444,    437,    426,
    424,    436,    1402,   429,    411,    386,    445,    440,    1370,   407,    398,    403,    404,    1371,
    435,    1390,   400,    428,    1388,   1394,   1379,   1378,   377,    439,    414,    375,    434,    415,
    427,    368,    365,    433
]

trainNonAlcoholic = [
    450,    339,    396,    354,    370,    461,    351,    458,    451,    457,    379,    338,    364,    378,
    389,    382,    402,    356,    453,    394,    340,    371,    460,    346,    344,    355,    381,    459,
    395,    357,    456,    337,    367,    454,    359,    448,    392,    345,    348,    341
]

testAlcoholic = [
    369,    405,    406,    409,    410,    416,    417,    419,    421,    422,    423,    425,    430,    432,
    438,    443,    447,    1387,   1392
]

testNonAlcoholic = [
    450,    339,    396,    354,    370,    461,    351,    458,    451,    457,    379,    338,    364,    378,
    389,    382,    402,    356,    453,    394,    340,    371,    460,    346,    344,    355,    381,    459,
    395,    357,    456,    337,    367,    454,    359,    448,    392,    345,    348,    341
]


def get_column_names():
    column_names = ["Id", "Alcoholic", "Paradigm", "Replication", "Channel"]
    for i in range(256):
        column_names.append("Reading " + str(i+1))
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
    for i in range(1, len(users)):
        temp_users = all_users.append(read_file(users[i], alcoholic))
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


user = read_file(364, True)

readings = []
for i in range(256):
    readings.append("Reading " + str(i + 1))

user["Min"] = user[readings].min(axis=1)
user["Max"] = user[readings].max(axis=1)
user["Std"] = user[readings].std(axis=1)
user["Mean"] = user[readings].mean(axis=1)
user["Median"] = user[readings].median(axis=1)
user["Quantile025"] = user[readings].quantile(0.025, axis=1)
user["Quantile25"] = user[readings].quantile(0.25, axis=1)
user["Quantile75"] = user[readings].quantile(0.75, axis=1)
user["Quantile975"] = user[readings].quantile(0.975, axis=1)
user["IQR"] = user["Quantile75"] - user["Quantile25"]


user = user.drop(columns=readings)

print(user)
