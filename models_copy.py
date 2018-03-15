import pandas as pd
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def read_row_reduction_data(filename):
    # read data
    df = pd.read_csv(filepath_or_buffer='engineered/' + filename + '.csv',
                     header=None,
                     sep=",",
                     low_memory=False)

    df = df.loc[:, [1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    df.columns = ['Class', 'Min', 'Max', 'Sd', 'Mean', 'Median', 'IQR', 'Q(0.025)', 'Q(0.25)', 'Q(0.75)', 'Q(0.975)']
    return df


def read_column_reduction_data(filename):
    # read data
    df = pd.read_csv(filepath_or_buffer='engineered/' + filename + '.csv',
                     header=None,
                     sep=",")

    df = df.drop(df.columns[[0, 2, 3]], axis=1)
    return df


def append_train_files_columns():
    alcoholic_train = read_row_reduction_data('train_alcoholic_columns')
    non_alcoholic_train = read_row_reduction_data('train_non_alcoholic_columns')

    return alcoholic_train.append(non_alcoholic_train)

def append_train_files_rows():
    alcoholic_train = read_row_reduction_data('train_alcoholic_rows')
    non_alcoholic_train = read_row_reduction_data('train_non_alcoholic_rows')

    return alcoholic_train.append(non_alcoholic_train)

def append_test_files_columns():
    alcoholic_train = read_row_reduction_data('test_alcoholic_columns')
    non_alcoholic_train = read_row_reduction_data('test_non_alcoholic_columns')

    return alcoholic_train.append(non_alcoholic_train)

def append_test_files_rows():
    alcoholic_train = read_row_reduction_data('test_alcoholic_rows')
    non_alcoholic_train = read_row_reduction_data('test_non_alcoholic_rows')

    return alcoholic_train.append(non_alcoholic_train)

def plot_model(y_test, predictions):
    ## The line / model
    plt.scatter(y_test, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.show()

def model_columns():
    # Training set
    train = append_train_files_columns()

    X_train = train.ix[:, 1:]

    y_train = train.ix[:, :]
    y_train = pd.get_dummies(y_train)

    print(X_train)
    print(y_train)

    # Test set
    test = append_test_files_columns()

    X_test = test.ix[:, 1:]

    y_test = test.ix[:, :]
    y_test = pd.get_dummies(y_test)

    # Train model
    lr = linear_model.LinearRegression()
    model = lr.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = lr.predict(X_test)

    # The coefficients
    print('Coefficients: \n', lr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(y_test, y_pred))

    print(X_test['Min'].size)
    print(y_test.size)

    print('Model score:' + str(model.score(X_test, y_test)))

    plot_model(y_test, y_pred)
    # Plot outputs
    #plt.scatter(X_test['Min'], y_test,  color='black')
    #plt.plot(X_test['Min'], y_pred, color='blue', linewidth=3)

    #plt.xticks(())
    #plt.yticks(())

    #print(X_train)
    #print(X_test)

    #plt.scatter(lr.predict(X_train), lr.predict(X_train) - y_train, c='blue', alpha=0.5)
    #plt.scatter(lr.predict(X_test), lr.predict(X_test) - y_test, c='green', s=40)

    #plt.hlines(y=0, xmin=-20, xmax=20)
    #plt.show()

def model_rows():
    # Training set
    train = append_train_files_rows()

    X_train = train.ix[:, 1:]

    y_train = train.ix[:, :]
    y_train = pd.get_dummies(y_train)

    print(X_train)
    print(y_train)

    # Test set
    test = append_test_files_rows()

    X_test = test.ix[:, 1:]

    y_test = test.ix[:, :]
    y_test = pd.get_dummies(y_test)

    # Train model
    lr = linear_model.LinearRegression()
    model = lr.fit(X_train, y_train)

    # Make predictions using the testing set
    y_pred = lr.predict(X_test)

    # The coefficients
    print('Coefficients: \n', lr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    print('Variance score: %.2f' % r2_score(y_test, y_pred))

    print(X_test['Min'].size)
    print(y_test.size)

    print('Model score:' + str(model.score(X_test, y_test)))

    plot_model(y_test, y_pred)

model_rows()