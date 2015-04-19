import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
species = iris.target_names[iris.target]
iris = pd.DataFrame(np.column_stack((iris.data, species)),
                    columns=iris.feature_names + ['species'])
iris.reset_index()              # include ID (index) as data
iris.to_csv('iris.csv')         # write without internal index

iris.iloc[7, 2] = 1.6
print iris.iloc[7, 2]
iris.to_csv('iris_one_change.csv', index=False)
