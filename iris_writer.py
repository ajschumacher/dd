import numpy as np
import pandas as pd
from sklearn import datasets

iris = datasets.load_iris()
species = iris.target_names[iris.target]
iris = pd.DataFrame(np.column_stack((iris.data, species)),
                    columns=iris.feature_names + ['species'])
iris.reset_index()
