import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


def read_row_reduction_data(filename):
    # read data
    df = pd.read_csv(filepath_or_buffer='engineered/' + filename + '.csv',
                     header=None,
                     sep=",",
                     low_memory=False)

    df = df.loc[:, [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    df.columns = ['Class', 'Experiment Type', 'Min', 'Max', 'Sd', 'Mean', 'Median', 'IQR', 'Q(0.025)', 'Q(0.25)', 'Q(0.75)', 'Q(0.975)']
    return df


def read_column_reduction_data(filename):
    # read data
    df = pd.read_csv(filepath_or_buffer='engineered/' + filename + '.csv',
                     header=None,
                     sep=",")

    df = df.drop(df.columns[[0, 2, 3]], axis=1)
    return df


def append_train_files():
    alcoholic_train = read_row_reduction_data('train_alcoholic_columns')
    non_alcoholic_train = read_row_reduction_data('train_non_alcoholic_columns')

    return alcoholic_train.append(non_alcoholic_train)

def append_test_files():
    alcoholic_train = read_row_reduction_data('test_alcoholic_columns')
    non_alcoholic_train = read_row_reduction_data('test_non_alcoholic_columns')

    return alcoholic_train.append(non_alcoholic_train)

def plot_model(y_test, predictions):

    print(sklearn.metrics.confusion_matrix(y_test, predictions, labels=[True, False]))

    ## The line / model
    plt.scatter(y_test, predictions)
    plt.xlabel('True Values')
    plt.ylabel('Predictions')
    plt.show()


# Training set
train = append_train_files()

X_train = train.ix[:, 5:6]

y_train = train.ix[:, 0:1]
y_train = pd.get_dummies(y_train)
y_train = y_train.iloc[:, 0:1]

#y_train = y_train.ix[:, 10:11]
print(y_train)
#print(y_train)

# Test set
test = append_test_files()

X_test = test.ix[:, 5:6]

y_test = test.ix[:, 0:1]
y_test = pd.get_dummies(y_test)
y_test = y_test.iloc[:, 0:1]

#y_test = np.array(test.ix[:, 10:11], dtype=bool)
print(y_test)

# Train model
#lr = linear_model.LinearRegression()
lr = linear_model.LogisticRegression(C=1e5)
model = lr.fit(X_train, y_train)

# Make predictions using the testing set
y_pred = lr.predict(X_test);

# The coefficients
print('Coefficients: \n', lr.coef_)
# The mean squared error
print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))

#print(X_test['Min'].size)
#print(y_test.size)

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
#plt.scatter(lr.predict(X_test), y_pred - y_test, c='green', s=40)

#plt.hlines(y=0, xmin=-20, xmax=20)
#plt.show()

