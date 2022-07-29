# Nosql Database Modelling, Implementation and Querying Using MongoDB
----
---

Using the terminal on MacOS csv data compiled from the pollution database on the mysqldb was used to populate a MongoDB, in JSON format and only including readings from one station(Colston Avenue). This was done using the Mongodb language
## Implementation Steps
-----
---
#### Starting mongodb and creating a database with two collections readings & station
---
==Command== 
mongosh # Starts mongodb
==output==
Current Mongosh Log ID:	6261536780fb809cbbec5dce
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.3.1
Using MongoDB:		5.0.7
Using Mongosh:		1.3.1

For mongosh info see: https://docs.mongodb.com/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.


   The server generated these startup warnings when booting:
   2022-04-21T13:50:11.558+01:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2022-04-21T13:50:11.559+01:00: You are running this process as the root user, which is not recommended
   2022-04-21T13:50:11.559+01:00: This server is bound to localhost. Remote systems will be unable to connect to this server. Start the server with --bind_ip <address> to specify which IP addresses it should serve responses from, or with --bind_ip_all to bind to all interfaces. If this behavior is desired, start the server with --bind_ip 127.0.0.1 to disable this warning
   2022-04-21T13:50:11.559+01:00: Soft rlimits for open file descriptors too low

==Command==
test> use pollution-db3 # Switiching default database to pollution-db3
==output==
switched to db pollution-db3

==Command==
pollution-db3> db.createCollection('station')
pollution-db3> db.createCollection('readings')
pollution-db3> show collections

==Output==
readings
station 

### Modelling the data in json format and inserting queried data from mysqldb to include one station
-----
Creating a variable that holds station information
==Command== 
pollution-db3>  var station_data = {
 
"_id": 501,
"name": "Colston Avenue",
"geo_point": "(51.4552693825,-2.59664882861)"
 }
==Command== 
pollution-db3> db.station.insertOne(station_data)
==Output==
{ acknowledged: true, insertedId: 500 }

Ran this query in phpmyadmin 
==SQL code==
SELECT * FROM `readings` where `SiteID` = 501;
Exported the output rows to csv

Imported csv data to mongodb
==Command==
(base) iteoluwakiishiadegbite@kiishi-m1 dmf_assigment_answers % mongoimport -d pollution-db3 -c readings --file readings.csv --type csv --headerline
==Output==
2022-04-21T16:25:26.554+0100	connected to: mongodb://localhost/
2022-04-21T16:25:28.319+0100	34207 document(s) imported successfully. 0 document(s) failed to import.

Showed the first 3 rows of the readings
==Command==
pollution-db3> db.readings.find().limit(3)
==Output==
[
  {
    _id: ObjectId("62617766fef7c9b40bdc8276"),
    id: 2596,
    'Date Time': '2018-09-11T05:00:00+00:00',
    NOx: 'NULL',
    NO2: 'NULL',
    NO: 'NULL',
    SiteID: 501,
    PM10: 'NULL',
    NVPM10: 'NULL',
    VPM10: 'NULL',
    NVPM2: { '5': 'NULL' },
    PM2: { '5': 'NULL' },
    VPM2: { '5': 'NULL' },
    CO: 'NULL',
    O3: 'NULL',
    SO2: 'NULL',
    Temperature: 'NULL',
    RH: 'NULL',
    'Air Pressure': 'NULL',
    DateStart: '2018-11-30T00:00:00+00:00',
    DateEnd: 'NULL',
    Current: 1,
    'Instrument Type': 'Continuous (Reference)'
  },
  {
    _id: ObjectId("62617766fef7c9b40bdc8277"),
    id: 2637,
    'Date Time': '2018-09-09T05:00:00+00:00',
    NOx: 'NULL',
    NO2: 'NULL',
    NO: 'NULL',
    SiteID: 501,
    PM10: 'NULL',
    NVPM10: 'NULL',
    VPM10: 'NULL',
    NVPM2: { '5': 'NULL' },
    PM2: { '5': 'NULL' },
    VPM2: { '5': 'NULL' },
    CO: 'NULL',
    O3: 'NULL',
    SO2: 'NULL',
    Temperature: 'NULL',
    RH: 'NULL',
    'Air Pressure': 'NULL',
    DateStart: '2018-11-30T00:00:00+00:00',
    DateEnd: 'NULL',
    Current: 1,
    'Instrument Type': 'Continuous (Reference)'
  },
  {
    _id: ObjectId("62617766fef7c9b40bdc8278"),
    id: 2655,
    'Date Time': '2018-09-08T05:00:00+00:00',
    NOx: 'NULL',
    NO2: 'NULL',
    NO: 'NULL',
    SiteID: 501,
    PM10: 'NULL',
    NVPM10: 'NULL',
    VPM10: 'NULL',
    NVPM2: { '5': 'NULL' },
    PM2: { '5': 'NULL' },
    VPM2: { '5': 'NULL' },
    CO: 'NULL',
    O3: 'NULL',
    SO2: 'NULL',
    Temperature: 'NULL',
    RH: 'NULL',
    'Air Pressure': 'NULL',
    DateStart: '2018-11-30T00:00:00+00:00',
    DateEnd: 'NULL',
    Current: 1,
    'Instrument Type': 'Continuous (Reference)'
  }
]

Used an aggregate function from the referencing model to populate the station collection in a json format
==Command== 
db.station.aggregate([
...     {
.....         $lookup: {
.......             from: "readings",
.......             localField: "_id",
.......             foreignField: "SiteID",
.......             as: "readings"
.......         }
.....     }
... ]).pretty();
==Output==
[
  {
    _id: 501,
    name: 'Colston Avenue',
    geo_point: '(51.4552693825,-2.59664882861)',
    readings: [
      {
        _id: ObjectId("62617766fef7c9b40bdc8276"),
        id: 2596,
        'Date Time': '2018-09-11T05:00:00+00:00',
        NOx: 'NULL',
        NO2: 'NULL',
        NO: 'NULL',
        SiteID: 501,
        PM10: 'NULL',
        NVPM10: 'NULL',
        VPM10: 'NULL',
        NVPM2: { '5': 'NULL' },
        PM2: { '5': 'NULL' },
        VPM2: { '5': 'NULL' },
        CO: 'NULL',
        O3: 'NULL',
        SO2: 'NULL',
        Temperature: 'NULL',
        RH: 'NULL',
        'Air Pressure': 'NULL',
        DateStart: '2018-11-30T00:00:00+00:00',
        DateEnd: 'NULL',
        Current: 1,
        'Instrument Type': 'Continuous (Reference)'
      },
      {
        _id: ObjectId("62617766fef7c9b40bdc8277"),
        id: 2637,
        'Date Time': '2018-09-09T05:00:00+00:00',
        NOx: 'NULL',
        NO2: 'NULL',
        NO: 'NULL',
        SiteID: 501,
        PM10: 'NULL',
        NVPM10: 'NULL',
        VPM10: 'NULL',
        NVPM2: { '5': 'NULL' },
        PM2: { '5': 'NULL' },
        VPM2: { '5': 'NULL' },
        CO: 'NULL',
        O3: 'NULL',
        SO2: 'NULL',
        Temperature: 'NULL',
        RH: 'NULL',
        'Air Pressure': 'NULL',
        DateStart: '2018-11-30T00:00:00+00:00',
        DateEnd: 'NULL',
        Current: 1,
        'Instrument Type': 'Continuous (Reference)'
      },











docker run -d -p 8000:8080 --restart=always --cap-add=SYS_ADMIN --name=dillinger <yourus