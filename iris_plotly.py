import pandas as pd

df = pd.read_csv(
    filepath_or_buffer='https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data',
    header=None,
    sep=',')

df.columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class']

# split data table into data X and class labels y

X = df.ix[:, 0:4].values
y = df.ix[:, 4].values

print(df.values)

df = pd.DataFrame(df.values, columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid', 'class'])

from sklearn.preprocessing import StandardScaler
X_std = StandardScaler().fit_transform(X)

# normalize data
from sklearn import preprocessing
data_scaled = pd.DataFrame(preprocessing.scale(X), columns=['sepal_len', 'sepal_wid', 'petal_len', 'petal_wid'])

from sklearn.decomposition import PCA as sklearnPCA
sklearn_pca = sklearnPCA(svd_solver='auto')
Y_sklearn = sklearn_pca.fit_transform(X_std)


#print pd.DataFrame(sklearn_pca.components_, columns=data_scaled.columns)
print(sklearn_pca.n_components_)
print pd.DataFrame(sklearn_pca.components_, columns=data_scaled.columns) # ?
print pd.DataFrame(sklearn_pca.explained_variance_ratio_) # % of information
print pd.DataFrame(sklearn_pca.explained_variance_) #Eigenvalues
print(sum(sklearn_pca.explained_variance_ratio_))



