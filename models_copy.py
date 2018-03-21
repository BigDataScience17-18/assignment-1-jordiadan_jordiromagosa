import pandas as pd
from sklearn import linear_model, metrics
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def read_data(filename):
    # read data
    return pd.read_csv(filepath_or_buffer='model_files/' + filename + '.csv',
                       sep=",",
                       low_memory=False)


def print_outcome_variables(data):
    outcomes = data['Alcoholic'].value_counts()
    print(outcomes)


def plot_model(y_test, predictions):
    print(metrics.confusion_matrix(y_test, predictions))

    ## The line / model
    plt.scatter(y_test, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.show()


def model_columns():
    # Training set
    train = read_data('train_1_columns')

    train.drop(train.columns[[0, 2, 3]], axis=1, inplace=True)
    X_train = train.ix[:, 1:]

    y_train = train["Alcoholic"]
    y_train = pd.get_dummies(y_train)

    print(X_train)
    print(y_train)

    # Test set
    test = read_data('test_1_columns')

    test.drop(test.columns[[0, 2, 3]], axis=1, inplace=True)
    X_test = test.ix[:, 1:]

    y_test = test["Alcoholic"]
    # y_test = pd.get_dummies(y_test)

    # Train model
    # lr = linear_model.LinearRegression()
    lr = linear_model.LogisticRegression()
    model = lr.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = lr.predict(X_test)

    # The coefficients
    print('Coefficients: \n', lr.coef_)
    # The mean squared error
    # print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    # print('Variance score: %.2f' % r2_score(y_test, y_pred))

    # print(X_test['Min'].size)
    print(y_test.size)

    print('Model score:' + str(model.score(X_test, y_test)))

    plot_model(y_test, y_pred)


def model_rows():
    # Training set
    train = read_data('train_1_rows')

    print_outcome_variables(train)

    # train.drop(train.columns[[0, 2, 4]], axis=1, inplace=True)
    train.drop(train.columns[[0]], axis=1, inplace=True)

    print(train)

    X_train = train.ix[:, 1:]
    X_train = pd.get_dummies(X_train)
    y_train = train["Alcoholic"]
    # y_train = pd.get_dummies(y_train)


    # Test set
    test = read_data('test_1_rows')

    test.drop(test.columns[[0]], axis=1, inplace=True)
    X_test = test.ix[:, 1:]
    X_test = pd.get_dummies(X_test)
    y_test = test["Alcoholic"]

    # Train model
    lr = linear_model.LogisticRegression(C=1e5)
    model = lr.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = lr.predict(X_test)

    # The coefficients
    print('Coefficients: \n', lr.coef_)
    # The mean squared error
    # print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    # print('Variance score: %.2f' % r2_score(y_test, y_pred))

    # print(X_test['Min'].size)
    print(y_test.size)

    print('Model score:' + str(model.score(X_test, y_test)))

    plot_model(y_test, y_pred)


# model_columns()
model_rows()
