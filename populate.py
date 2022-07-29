import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import exc

# try:
# connection tool to connect to the database pollution-db2, which was created earlier
engine = create_engine("mysql+pymysql://{user}:{pw}@localhost:{port}/{database}"
                       .format(user = 'root',
                               pw ="helloworld",
                               port=8806,
                               database = "pollution-db2"))

schema = [{'measure': 'Date Time', 'desc': 'date and time of measurement','unit': 'datetime'},
          {'measure':'NOx', 'desc':"Concentration of oxides of nitrogen",'unit':'㎍/m3'},
          {'measure':'NO2', 'desc':'Concentration of nitrogen dioxide' , 'unit':'㎍/m3'},
          {'measure':'NO'  , 'desc':'Concentration of nitric oxide' , 'unit':'㎍/m3' },
          {'measure':'SiteID', 'desc':'Site ID for the station', 'unit':'integer'},
          {'measure':'PM10', 'desc':'Concentration of particulate matter <10 micron diameter', 'unit':'㎍/m3'},
          {'measure':'NVPM10', 'desc':'Concentration of non - volatile particulate matter <10 micron diameter', 'unit':'㎍/m3'},
          {'measure':'VPM10', 'desc':'Concentration of volatile particulate matter <10 micron diameter', 'unit':'㎍/m3'},
          {'measure':'NVPM2.5', 'desc':'Concentration of non volatile particulate matter <2.5 micron diameter', 'unit':'㎍/m3'},
          {'measure':'PM2.5', 'desc':'Concentration of particulate matter <2.5 micron diameter', 'unit':'㎍/m3'},
          {'measure':'VPM2.5', 'desc':'Concentration of volatile particulate matter <2.5 micron diameter', 'unit':'㎍/m3'},
          {'measure':'CO', 'desc':'Concentration of carbon monoxide', 'unit':'㎎/m3'},
          {'measure':'O3', 'desc':'Concentration of ozone', 'unit':'㎍/m3'},
          {'measure':'SO2', 'desc':'Concentration of sulphur dioxide', 'unit':'㎍/m3'},
          {'measure':'Temperature', 'desc':'Air temperature', 'unit':'°C'},
          {'measure':'RH', 'desc':'Relative Humidity', 'unit':'%'},
          {'measure':'Air Pressure', 'desc':'Air Pressure', 'unit':'mbar'},
          {'measure':'Location', 'desc':'Text description of location', 'unit':'text'},
          {'measure':'geo_point_2d', 'desc':'Latitude and longitude', 'unit':'geo point'},
          {'measure':'DateStart', 'desc':'The date monitoring started', 'unit':'datetime'},
          {'measure':'DateEnd', 'desc':'The date monitoring ended', 'unit':'datetime'},
          {'measure':'Current', 'desc':'Is the monitor currently operating', 'unit':'text'},
          {'measure':'Instrument Type', 'desc':'Classification of the instrument', 'unit':'text'}]


# Manually made  a station dictionary to give a template when populating the database
station = [
    {'name': 'AURN Bristol Centre', 'id': 188, "geo_point_2d":''},
    {'name': 'Brislington Depot', 'id': 203,"geo_point_2d": '51.4417471802,-2.55995583224'},
    {'name': 'Rupert Street', 'id': 206, "geo_point_2d":'51.4554331987,-2.59626237324'},
    {'name': 'IKEA M32', 'id': 209, "geo_point_2d":''},
    {'name': 'Old Market', 'id': 213, "geo_point_2d":'51.4560189999,-2.58348949026'},
    {'name': 'Parson Street School', 'id': 215, "geo_point_2d":'51.432675707,-2.60495665673'},
    {'name': 'Temple Meads Station', 'id': 228, "geo_point_2d":''},
    {'name': 'Wells Road', 'id': 270, "geo_point_2d":'51.4278638883,-2.56374153315'},
    {'name': 'Trailer Portway P&R', 'id': 271, "geo_point_2d":''},
    {'name': 'Newfoundland Road Police Station', 'id': 375, "geo_point_2d":'51.4606738207,-2.58225341824'},
    {'name': "Shiner's Garage", 'id': 395, "geo_point_2d":'51.4577930324,-2.56271419977'},
    {'name': 'AURN St Pauls', 'id': 452, "geo_point_2d" : '51.4628294172,-2.58454081635'},
    {'name': 'Bath Road', 'id': 447, "geo_point_2d":'51.4425372726,-2.57137536073'},
    {'name': 'Cheltenham Road \ Station Road', 'id': 459, "geo_point_2d":'51.4689385901,-2.5927241667'},
    {'name': 'Fishponds Road', 'id': 463, "geo_point_2d":'51.4780449714,-2.53523027459'},
    {'name': 'CREATE Centre Roof', 'id': 481, "geo_point_2d":'51.447213417,-2.62247405516'},
    {'name': 'Temple Way', 'id': 500, "geo_point_2d":'51.4579497129,-2.58398909033'},
    {'name': 'Colston Avenue', 'id': 501, "geo_point_2d":'51.4552693825,-2.59664882861'}]


station_dataframe = pd.DataFrame(station)
station_dataframe.to_sql('station', con = engine, if_exists= 'replace')

readings = pd.read_csv('clean.csv', sep = ';', low_memory= True)
pd.to_datetime(readings['Date Time'])
readings.drop(columns = ['Location', 'geo_point_2d'], axis =1, inplace = True)
readings.rename(columns = {'SiteID': 'station_id'})

readings.to_sql('readings', con = engine, if_exists= 'append', chunksize=1000, index_label="id")

schema_df = pd.DataFrame(schema)
schema_df.to_sql('schema', con  = engine, if_exists= 'replace')
