import pymysql as pm

import sys

try:
    #connect to mysql
    conn = pm.connect(host = 'localhost', user = 'root', passwd = "helloworld", port = 8806)

    #create the cursor
    cur = conn.cursor()

     # executing the cursor with the sql string command
    cur.execute('SELECT * FROM `pollution-db2`. `readings` LIMIT 100;')

    # gets the results and indexes it as a list
    results = cur.fetchall()

    # create insert-100.sql to write insert statements
    insert_file = open('insert-100.sql', 'w')

    # iterate over the 100  results and create an sql statement
    for  r in results:
        print(r)
        sql_insert = """
                INSERT INTO `pollution-db2`.`reading`
                (`Date Time`, `NOx`, `NO2`,`NO`,`station_id`, `PM10`, `NVPM10`, `VPM10`, `NVPM2.5`, `PM2.5`, `VPM2.5`,`CO`, `O3`, 
                 `SO2`, `Temperature`, `RH`, `Air Pressure`,  `DateStart`,`DateEnd`,`Current`, `Instrument Type`)
                  VALUES  ('{datetime}',{nox},{no2},{no},{station_id},{pm10},{nvpm10},{vpm10},{nvpm2_5},{pm2_5},{vpm2_5},{co},{o3}
                  ,{so2}, {temperature}, {rh},{air_pressure}, '{datestart}','{dateend}', {current}, '{instrument_type}')""".format(
            datetime = r[1],
            nox = r[2],
            no2 = r[3],
            no = r[4],
            station_id =r[5],
            pm10 =  r[6],
            nvpm10 = r[7],
            vpm10 = r[8],
            nvpm2_5 = r[9],
            pm2_5 = r[10],
            vpm2_5 = r[11],
            co = r[12],
            o3 = r[13],
            so2 =  r[14],
            temperature =r[15],
            rh = r[16],
            air_pressure = r[17],
            datestart = r[18],
            dateend = r[19],
            current = r[20],
            instrument_type = r[21]
         )
        insert_file.write(sql_insert)
    conn.close()
    insert_file.close()

except BaseException as err:
    print(f"an error occured: {err}")