import numpy as np
import pandas as pd
label = pd.read_csv('123_filtered 1.csv')
train_data=label.values
y = train_data[:,0]
y=y.astype(float)
print(y)