import pandas as pd
from sklearn import linear_model, metrics
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, classification_report


def read_data(filename):
    # read data
    return pd.read_csv(filepath_or_buffer='model_files/' + filename + '.csv',
                       sep=",",
                       low_memory=False)

def plot_model(y_test, predictions):
    print(metrics.confusion_matrix(y_test, predictions))

    ## The line / model
    plt.scatter(y_test, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.show()


def logistic_regression_model_and_plot(filename_train, filename_test, x_columns_names, y_columns_names):
    # Training set
    train_data = pd.read_csv(filepath_or_buffer=filename_train, sep=",", low_memory=False)
    x_train = pd.get_dummies(train_data[x_columns_names])
    y_train = pd.get_dummies(train_data[y_columns_names])
    print(x_train)
    print(y_train)

    # Test set
    test_data = pd.read_csv(filepath_or_buffer=filename_test, sep=",", low_memory=False)
    x_test = pd.get_dummies(test_data[x_columns_names])
    y_test = pd.get_dummies(test_data[y_columns_names])
    print(x_test)
    print(y_test)

    # Train model
    lr = linear_model.LogisticRegression()
    model = lr.fit(x_train, y_train)

    # Make predictions using the testing set
    y_pred = lr.predict(x_test)

    # The coefficients
    # print('Coefficients: \n', lr.coef_)
    # The mean squared error
    # print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # Explained variance score: 1 is perfect prediction
    # print('Variance score: %.2f' % r2_score(y_test, y_pred))

    print('Model score:' + str(model.score(x_test, y_test)))
    print(classification_report(y_test, y_pred))

    plot_model(y_test, y_pred)


#x_columns = ["Paradigm", "Replication", "Channel", 'Min', 'Max', 'Sd', 'Mean', 'Median', 'IQR', 'Q(0.025)', 'Q(0.25)', 'Q(0.75)', 'Q(0.975)']
#y_columns = ["Alcoholic"]

#logistic_regression_model_and_plot("model_files/train_1_rows.csv", "model_files/test_1_rows.csv", x_columns, y_columns)


x_columns = ["Paradigm", "Channel"]
for reading in range(256):
    x_columns.append("Reading " + str(reading+1))
y_columns = ["Alcoholic"]

logistic_regression_model_and_plot("model_files/train_1_columns.csv", "model_files/test_1_columns.csv", x_columns, y_columns)

