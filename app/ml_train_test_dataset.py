#unsupervisioned machine leaning
#clustering data
#k-means

import dataset_explorator

from sklearn import linear_model

dataframe = dataset_explorator.read_dataframe()

print(dataframe.head())

reg = linear_model.LinearRegression()

reg.fit([[0,0],[1,1], [2,2]],[0,1,2])

print(reg.coef_)
