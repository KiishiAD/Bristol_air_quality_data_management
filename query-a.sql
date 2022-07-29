SELECT `Date Time`, station.name, NOx 
FROM readings, station 
WHERE NOx = ( SELECT max(NOx) FROM readings r WHERE `Date Time`>= '2019-01-01' and `Date Time` <= '2019-12-31') 
and station.id = readings.SiteID;