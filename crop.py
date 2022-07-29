
import pandas as pd

df=pd.read_csv('bristol-air-quality-data.csv', sep = ';') # read in the csv file and highlighted the delimeter using sep



df= df[df['Date Time'].str[:4] >='2010']#This keeps the rows that have dates past or equals to 2010

print(df.sort_values(by = 'Date Time', ascending = True).head(100))#Keeps the data in ascending order, to check if there is no record before 2010


# In[15]:


crop_data= df
crop_data.to_csv('crop.csv',index = False, sep=';')#generates a cropped csv

