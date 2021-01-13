# -*- coding: utf-8 -*-
"""DataExploration.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cJKTK9mg4EjFnVG8C6meVwM-JnVKzD2j
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from google.colab import files
uploaded = files.upload()

data = pd.read_csv('Health_Opportunity_Index.csv')

data.head()

data.info()

data.isna().sum()

sns.pairplot(data)

corr = data.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask)

print(corr['Health Opportunity Index'])

sns.scatterplot(data["Employment Accessibility"], data["Economic Opportunity Profile"])

sns.jointplot(data["Population Churning"], data["Community Environment Profile"], kind="hex")

from sklearn.linear_model import LinearRegression
X = data["Employment Accessibility"].to_numpy().reshape(-1, 1)
y = data["Economic Opportunity Profile"].to_numpy().reshape(-1, 1)

reg = LinearRegression().fit(X, y)
reg.score(X, y)

xfit = np.linspace(0, 0.8, 100)
yfit = reg.predict(xfit[:, np.newaxis])

plt.scatter(X, y, edgecolors='b')
plt.plot(xfit, yfit)
plt.show()

from sklearn.model_selection import train_test_split
# Split the data into train set (80%) and test set (20%)
X_train, X_test, y_train, y_test = train_test_split(data[['Census Tract','Community Environment Profile','Material Deprivation','Income Inequality']], 
                                                    data[['Health Opportunity Index']], test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
sk_pred_normal = lin_reg.predict(X_test)
mse2 = mean_squared_error(y_test, sk_pred_normal)
sk_normal_rmse = np.sqrt(mse2)
print(" ")
print("SkLearn Normal RMSE %f" % sk_normal_rmse)

from sklearn.ensemble import RandomForestRegressor

forest_reg = RandomForestRegressor(n_estimators=100, random_state=42)
forest_reg.fit(X_train, y_train)

housing_predictions = forest_reg.predict(X_test)
forest_mse = mean_squared_error(y_test, housing_predictions)
forest_rmse = np.sqrt(forest_mse)
forest_rmse



X_traintf, X_testtf, y_traintf, y_testtf = train_test_split(data[['Rural~Urban', 'Census Tract', 'Access to Care', 'Employment Accessibility', 'Affordability', 'Air Quality', 'Population Churning', 'Education', 'Food Accessibility', 'Income Inequality', 'Job Participation', 'Population Density', 'Segregation', 'Material Deprivation', 'Walkability', 'Community Environment Profile', 'Consumer Opportunity Profile', 'Economic Opportunity Profile', 'Wellness Disparity Profile']], 
                                                    data[['Health Opportunity Index']], test_size=0.2, random_state=42)






from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

x_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        #('std_scaler', StandardScaler()),
])
full_pipeline = ColumnTransformer([
        ("one Hot", OneHotEncoder(),['Rural~Urban']),
        ("x_vals", x_pipeline, ['Census Tract', 'Access to Care', 'Employment Accessibility', 'Affordability', 'Air Quality', 'Population Churning', 'Education', 'Food Accessibility', 'Income Inequality', 'Job Participation', 'Population Density', 'Segregation', 'Material Deprivation', 'Walkability', 'Community Environment Profile', 'Consumer Opportunity Profile', 'Economic Opportunity Profile', 'Wellness Disparity Profile']),
])





X_traintf2 = full_pipeline.fit_transform(X_traintf)
X_testtf2 = full_pipeline.fit_transform(X_testtf)

y_traintf2 = y_traintf.to_numpy()
y_testtf2 = y_testtf.to_numpy()

import tensorflow as tf

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(20,)))
model.add(tf.keras.layers.Dense(128, activation='tanh'))
model.add(tf.keras.layers.Dense(128, activation='tanh'))
model.add(tf.keras.layers.Dense(1))

model.compile(optimizer='adam', loss='mse')
model.fit(X_traintf2, y_traintf2, epochs=100, verbose=0)

tensor_predictions = model.predict(X_testtf2)

tensor_mse = mean_squared_error(y_testtf2, tensor_predictions)
tensor_rmse = np.sqrt(tensor_mse)
tensor_rmse

forest_reg = RandomForestRegressor(n_estimators=100, random_state=42)
forest_reg.fit(X_traintf2, y_traintf2)

housing_predictions = forest_reg.predict(X_testtf2)
forest_mse = mean_squared_error(y_testtf2, housing_predictions)
forest_rmse = np.sqrt(forest_mse)
forest_rmse

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

lin_reg = LinearRegression()
lin_reg.fit(X_traintf2, y_traintf2)
sk_pred_normal = lin_reg.predict(X_testtf2)
mse2 = mean_squared_error(y_testtf2, sk_pred_normal)
sk_normal_rmse = np.sqrt(mse2)
print(" ")
print("SkLearn Normal RMSE %f" % sk_normal_rmse)

poopoo = ['rural', 'urban', 'Census Tract', 'Access to Care', 'Employment Accessibility', 'Affordability', 'Air Quality', 'Population Churning', 'Education', 'Food Accessibility', 'Income Inequality', 'Job Participation', 'Population Density', 'Segregation', 'Material Deprivation', 'Walkability', 'Community Environment Profile', 'Consumer Opportunity Profile', 'Economic Opportunity Profile', 'Wellness Disparity Profile']



print(lin_reg.coef_)

for i in range (20):
  print(poopoo[i])
  print(lin_reg.coef_[:,i])

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


x_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        #('std_scaler', StandardScaler()),
])
full_pipeline = ColumnTransformer([
        ("one Hot", OneHotEncoder(),['Rural~Urban']),
        ("x_vals", x_pipeline, ['Health Opportunity Index', 'Access to Care', 'Employment Accessibility', 'Affordability', 'Air Quality', 'Population Churning', 'Education', 'Food Accessibility', 'Income Inequality', 'Job Participation', 'Population Density', 'Segregation', 'Material Deprivation', 'Walkability', 'Community Environment Profile', 'Consumer Opportunity Profile', 'Economic Opportunity Profile', 'Wellness Disparity Profile']),
])


data.head()

np_census = data.loc[:,['Census Tract']].to_numpy()

#np_dat = data.drop(columns=['Census Tract'])



np_dat = full_pipeline.fit_transform(data)

print(np_dat.shape)

from scipy.spatial import distance
def findClosest(censusID):

  smallest = np.Inf
  j = 0
  x = np.zeros(20)
  retVal = 0

  for i in np_dat:
    if (np_census[j] == censusID):
      x = i
      break
    j+=1
  j=0

  for i in np_dat:
    if (np_census[j] == censusID):
      continue
    dodo = distance.cosine(i, x)
    if (dodo < smallest):
      smallest = dodo
      retVal = np_census[j]
    j += 1

  return retVal

print(findClosest(51760040300))

from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder


x_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        ('std_scaler', StandardScaler()),
])

full_pipeline = ColumnTransformer([
        ("one Hot", OneHotEncoder(),['Rural~Urban']),
        ("x_vals", x_pipeline, ['Access to Care', 'Employment Accessibility', 
                                'Affordability', 'Air Quality', 'Population Churning', 
                                'Education', 'Food Accessibility', 'Income Inequality', 
                                'Job Participation', 'Population Density', 'Segregation', 
                                'Material Deprivation', 'Walkability', 'Community Environment Profile',
                                'Consumer Opportunity Profile', 'Economic Opportunity Profile', 
                                'Wellness Disparity Profile', 'Health Opportunity Index']),
])





numpy_data = full_pipeline.fit_transform(data)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4, random_state=0).fit(numpy_data)
y_kmeans = kmeans.predict(numpy_data)



from sklearn.cluster import KMeans
from matplotlib import pyplot as plt

X = numpy_data
distorsions = []
for k in range(2, 20):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(X)
    distorsions.append(kmeans.inertia_)

fig = plt.figure(figsize=(15, 5))
plt.plot(range(2, 20), distorsions)
plt.grid(True)
plt.title('Elbow curve')

def health_buckets(x):
  if 0 <= x < 0.2:
    return 0
  elif 0.2 <= x < 0.4:
    return 1
  elif 0.4 <= x < 0.6:
    return 2
  elif 0.6 <= x < 0.8:
    return 3
  else:
    return 4

data['buckets'] = data['Health Opportunity Index'].apply(lambda x: health_buckets(x))

data.head()

from sklearn.model_selection import train_test_split
X_traintf, X_testtf, y_traintf, y_testtf = train_test_split(data[['Rural~Urban', 'Census Tract', 'Access to Care', 'Employment Accessibility', 'Affordability', 'Air Quality', 'Population Churning', 'Education', 'Food Accessibility', 'Income Inequality', 'Job Participation', 'Population Density', 'Segregation', 'Material Deprivation', 'Walkability', 'Community Environment Profile', 'Consumer Opportunity Profile', 'Economic Opportunity Profile', 'Wellness Disparity Profile']], 
                                                    data[['buckets']], test_size=0.2, random_state=42)






from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder

x_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy="median")),
        #('std_scaler', StandardScaler()),
])
full_pipeline = ColumnTransformer([
        ("one Hot", OneHotEncoder(),['Rural~Urban']),
        ("x_vals", x_pipeline, ['Census Tract', 'Access to Care', 'Employment Accessibility', 'Affordability', 'Air Quality', 'Population Churning', 'Education', 'Food Accessibility', 'Income Inequality', 'Job Participation', 'Population Density', 'Segregation', 'Material Deprivation', 'Walkability', 'Community Environment Profile', 'Consumer Opportunity Profile', 'Economic Opportunity Profile', 'Wellness Disparity Profile']),
])





X_traintf2 = full_pipeline.fit_transform(X_traintf)
X_testtf2 = full_pipeline.fit_transform(X_testtf)

y_traintf2 = y_traintf.to_numpy()
y_testtf2 = y_testtf.to_numpy()

model = tf.keras.models.Sequential()
model.add(tf.keras.Input(shape=(20,)))
model.add(tf.keras.layers.Dense(128, activation='tanh'))
model.add(tf.keras.layers.Dense(32, activation='tanh'))
model.add(tf.keras.layers.Dense(128))

model.compile(optimizer='adam',
              loss='mse',
              metrics=['accuracy'])
model.fit(X_traintf2, y_traintf2, epochs=50)

loss,acc = model.evaluate(x=X_testtf2, y=y_testtf2, verbose=2)
print("Restored model, accuracy: {:5.2f}%".format(100*acc))

