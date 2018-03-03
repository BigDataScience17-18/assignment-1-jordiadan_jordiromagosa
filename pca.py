import pandas as pd

#use H20 library to improve reading and processing data

# PCA with Row Reduction
#   columns = ['Min', 'Max', 'Sd', 'Mean', 'Median', 'IQR', 'Q(0.025)', 'Q(0.25)', 'Q(0.75)', 'Q(0.975)']
#   rows = Repetitions

df = pd.read_csv(filepath_or_buffer='engineered/train_alcoholic_columns.csv',
                 header=None,
                 sep=',',
                 low_memory=False)

df = df.loc[:, [1, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
df.columns = ['Class', 'Min', 'Max', 'Sd', 'Mean', 'Median', 'IQR', 'Q(0.025)', 'Q(0.25)', 'Q(0.75)', 'Q(0.975)']

# split data table into data X and class labels y

X = df.ix[:, 1:].values
y = df.ix[:, 0].values

print(X)
# print(y)

import plotly.plotly as py
from plotly.graph_objs import *
import plotly.tools as tls
#
# # Plotting histograms
# traces = []
#
# colors = {'Alcoholic': 'rgb(31, 119, 180)',
#           'No Alcoholic': 'rgb(255, 127, 14)'}
#
# for col in range(4):
#     for key in colors:
#         traces.append(Histogram(x=X[y==key, col],
#                         opacity=0.75,
#                         xaxis='x%s' %(col+1),
#                         marker=Marker(color=colors[key]),
#                         name=key,
#                         #showlegend=legend[col]
#                                  ))
# data = Data(traces)
#
# layout = Layout(barmode='overlay',
#                 xaxis=XAxis(domain=[0, 0.25], title='Min'),
#                 #xaxis2=XAxis(domain=[0.3, 0.5], title='Max'),
#                 #xaxis3=XAxis(domain=[0.55, 0.75], title='petal length (cm)'),
#                 #xaxis4=XAxis(domain=[0.8, 1], title='petal width (cm)'),
#                 yaxis=YAxis(title='count'),
#                 title='Distribution of the different Iris flower features')
#
# fig = Figure(data=data, layout=layout)
# py.iplot(fig)

#   Standarizing

from sklearn.preprocessing import StandardScaler

X_std = StandardScaler().fit_transform(X)

# print(X)
# print('\n')
# print(X_std)

# PCA in scikit-learn

from sklearn.decomposition import PCA as sklearnPCA

sklearn_pca = sklearnPCA(svd_solver='auto')
Y_sklearn = sklearn_pca.fit_transform(X_std)

#print(sklearn_pca.n_components_)
#print pd.DataFrame(sklearn_pca.components_, columns=df.columns[1:]) # ?
print pd.DataFrame(sklearn_pca.explained_variance_ratio_) # % of information
print(sum(sklearn_pca.explained_variance_ratio_))
#print pd.DataFrame(sklearn_pca.explained_variance_) #Eigenvalues