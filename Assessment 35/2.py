import numpy as np
from sklearn.impute import SimpleImputer

data = np.array([[1, 2, np.nan],
                 [4, np.nan, 6],
                 [7, 8, 9],
                 [np.nan, 5, 10]])

# Using SimpleImputer with the constant strategy
imputer = SimpleImputer(strategy='constant', fill_value=0)  # Replace missing values with 0
imputed_data = imputer.fit_transform(data)

print(imputed_data)