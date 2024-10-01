import pandas as pd
import numpy as np
print(pd.__version__)

df = pd.read_csv('laptops.csv')


# print(len(df))


# print(df.Brand.value_counts())
# print(df.isnull().sum())
#filtered_data = df[df['Brand'] == 'Dell']
#print(filtered_data['Final Price'].max())
#print(filtered_data)
#print(df.Screen.median())

#median_screen_size = df.Screen.median()
#filtered_df = df[df['Screen'] == 15.6]

#latest_row = filtered_df.tail(1)

#df['Screen'] = df['Screen'].fillna(latest_row['Screen'])

#new_median = df.Screen.median()
#print(new_median)

#filtered_data = df[df['Brand'] == 'Innjoo']
#print(filtered_data)
#new_df = filtered_data[['RAM', 'Storage', 'Screen']]
#new_df.drop_duplicates(inplace=True)
#X = new_df.values
#xtx = X.T.dot(X)
#inverse = np.linalg.inv(xtx)
#y = np.array([1100, 1300, 800, 900, 1000, 1100])

#x_inverse = inverse.dot(X.T)
#w = x_inverse.dot(y)
#print(np.sum(w))


rr_df = df[df['Brand'] == 'Innjoo']
rr_df = rr_df[['RAM', 'Storage', 'Screen']]
#rr_df.drop_duplicates(inplace=True)
X = rr_df.values
XTX = X.T.dot(X)
XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100])
XTXiXT = XTX_inv.dot(X.T)
w = XTXiXT.dot(y)
print(f"The w vector is: {w}")
print(f"[ANSWER-7] The first element of w is: {w[0]}")
