
#join tables matching time till second
select distinct locations.ist_time as time, aq.pm25 as pm25, aq.pm10 as pm10, locations.latitude as latitude , locations.longitude as longitude 
from locations, aq  
where locations.ist_time = aq.CreatedDate;

#by minute
select locations.utc_time, locations.ist_time, substr(locations.ist_time, 0, 17),aq.CreatedDate, aq.pm25, aq.pm10, locations.latitude, locations.longitude 
from locations, aq  
where substr(locations.ist_time, 0, 17) = substr(aq.CreatedDate,0,17)
order by locations.ist_time 


#get unique
select distinct substr(locations.ist_time, 0, 17), aq.pm25, aq.pm10, locations.latitude, locations.longitude 
from locations, aq  
where substr(locations.ist_time, 0, 17) = substr(aq.CreatedDate,0,17)
order by locations.ist_time 


select distinct substr(locations.ist_time, 0, 17), aq.pm25, aq.pm10, locations.latitude, locations.longitude 
from locations, aq  
where substr(locations.ist_time, 0, 17) = substr(aq.CreatedDate,0,17)
