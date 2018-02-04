import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff
import pandas as pd
import numpy as np


#plotly.tools.set_credentials_file(username='jadan', api_key='sW9G36YqG8WaLqCaVuF6')
plotly.tools.set_credentials_file(username='x2799830', api_key='R0ETv9zOSa7Hkc3t2Q0p')


# create table on plotly
df = pd.read_csv("results/co2a0000364.txt", sep=" ", lineterminator="\n", header=None)
table = ff.create_table(df)
#py.iplot(table, filename="table1")


#create bar graph
#filtered = df.iloc[:, 5:]
df.drop(df.columns[[0, 1, 2, 3, 4]], axis=1, inplace=True)
print(df)
#keys = np.array(filtered.keys)
voltage = np.array(df.values)
print(df.columns.values)
time = df.columns.values

for i in range(time):
    time[i] = (i - 4) * 3.906


data = [go.Bar(x=time,
               y=voltage)]
print(data)
#py.iplot(data, filename='basic_bar')


# py.plotly.iplot([trace1, trace2])