import pandas as pd

df = pd.read_csv('crop.csv', sep=';')


print(df.head())

# In[13]:


stations = [{'name': 'AURN Bristol Centre', 'id': 188},
            {'name': 'Brislington Depot', 'id': 203},
            {'name': 'Rupert Street', 'id': 206},
            {'name': 'IKEA M32', 'id': 209},
            {'name': 'Old Market', 'id': 213},
            {'name': 'Parson Street School', 'id': 215},
            {'name': 'Temple Meads Station', 'id': 228},
            {'name': 'Wells Road', 'id': 270},
            {'name': 'Trailer Portway P&R', 'id': 271},
            {'name': 'Newfoundland Road Police Station', 'id': 375},
            {'name': "Shiner's Garage", 'id': 395},
            {'name': 'AURN St Pauls', 'id': 452},
            {'name': 'Bath Road', 'id': 447},
            {'name': 'Cheltenham Road \ Station Road', 'id': 459},
            {'name': 'Fishponds Road', 'id': 463},
            {'name': 'CREATE Centre Roof', 'id': 481},
            {'name': 'Temple Way', 'id': 500},
            {'name': 'Colston Avenue', 'id': 501}] # Made a list of dictionaries  to identify the right IDs for the site location


def station_search(name, station_id): # defined a function to check if the parameters given are equal to the key values in the stations list of dictionaries
    for rows in stations:
        if name == rows['name'] and station_id == rows['id']:
            return True

cleaned_data= [] # Made a new list to append the cleaned data to

for index, row in df.iterrows(): #looped through the dataset and applied my station_search function,
    # outputting the mismatching and null values and appending the correct data to my previous list
    try:
        StationId = int(row.SiteID)
        StationName = row.Location
        if not station_search(StationName, StationId):
            print(StationId, StationName)
        else:
            cleaned_data.append(row)
    except IndexError as e:
        print(e)


df_new = pd.DataFrame(cleaned_data)
print(df_new.shape[0])
df_new.to_csv('clean.csv', sep =';',index= False)



