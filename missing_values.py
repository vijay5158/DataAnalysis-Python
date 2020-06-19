from sklearn.preprocessing import Imputer
import pandas as pd

data=pd.read_csv(r"C:\Users\Dell\Downloads\housing1\housing.csv")
#get description of data
print(data.info())
#call imputer object
imputer=Imputer(strategy="median")
#drop text attributes
data=data.drop("ocean_proximity",axis=1)
#fit imputer object to data
imputer.fit(data)
#apply imputer to dataset
data=imputer.transform(data)
data_pd=pd.DataFrame(data)
print(data_pd.info())
