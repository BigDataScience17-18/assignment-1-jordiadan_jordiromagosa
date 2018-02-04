import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np
from sklearn import preprocessing

## Exercise_1

# plotly.tools.set_credentials_file(username='jadan', api_key='sW9G36YqG8WaLqCaVuF6')
plotly.tools.set_credentials_file(username='x2799830', api_key='R0ETv9zOSa7Hkc3t2Q0p')

# create table on plotly
df = pd.read_csv("results/co2a0000364.txt", sep=" ", lineterminator="\n", header=None)
table = ff.create_table(df)
# py.iplot(table, filename="table1")


# create bar graph
df.drop(df.columns[[0, 1, 2, 3, 4]], axis=1, inplace=True)

# voltage = np.array(df.values)[0]
time = np.array(df.columns.values, dtype=float)

for i in range(0, len(time)):
    time[i] = (time[i] - 4) * 3.906

df.columns = time

#print(df)
# data = [go.Bar(x=time,
#                y=voltage)]
# py.iplot(data, filename='Exercise_1')


# py.plotly.iplot([trace1, trace2])

## Exercise 2
voltage = np.array(df.values)

# Create traces
trace0 = go.Scatter(
    x=time,
    y=voltage[0],
    mode='lines',
    name='FP1 - Channel 0'
)

trace1 = go.Scatter(
    x=time,
    y=voltage[1],
    mode='lines',
    name='FP2 - Channel 1'
)

trace2 = go.Scatter(
    x=time,
    y=voltage[2],
    mode='lines',
    name='F7 - Channel 2'
)

trace3 = go.Scatter(
    x=time,
    y=voltage[3],
    mode='lines',
    name='F8 - Channel 3'
)


#data = [trace0, trace1, trace2, trace3]

#py.iplot(data, filename='Exercise_2')


## Exercise_3

#print(df.columns.values)


data = [
    go.Surface(
        z=df.as_matrix()
    )
]


layout = go.Layout(
    title='Exercise 3',
    autosize=True,
)
fig = go.Figure(data=data, layout=layout)
#py.iplot(fig, filename='Exercise 3')


#X''
df_norm = (df - df.mean()) / (df.max() - df.min())
#print(df_norm)

# Xi

# X mean of all the channels
mean = df_norm.mean()
#print(mean)

# Xmed median fromm all the channels

# Xi' = Xi - X
x = df.mean() - df.median()
#print(x)

test = df_norm.max() - df_norm.min()
#print(test)

#quantiles

first = df.quantile(.25)
second = df.quantile(.5)
third = df.quantile(.75)

print(first)
print(second)
print(third)


