SELECT station.name, AVG(`readings`.`vpm2.5`), AVG(`readings`.`pm2.5`) from readings, station where readings.SiteID = station.id and year(`readings`.`Date Time`) >= '2010-01-01' 
and year(`readings`.`Date Time`) <= '2019-12-31' 
and readings.`Date Time` LIKE '%08:00:00+00:00' GROUP BY station.name;
