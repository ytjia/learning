-- 通过地理位置过滤出特定高校的学生

-- v0.1北京大学20131101上报的终端
SELECT DISTINCT
    uuid
FROM
    log.mobile_data_location
WHERE
    dt = '20131101'
    AND marslat > 39.98714 AND marslat < 39.996889
    AND marslng > 116.304849 AND marslng < 116.315235

--
select
    *
from
    (select
        uuid,
        (case 
            when marslat > 39.98714 and marslat < 39.996889 and marslng > 116.304849 and marslng < 116.315235
            then 'PKU'
            when acos(sin(marslat*pi/180)*sin(40.001137*pi/180) + cos(marslat*pi/180)*cos(40.001137*pi/180)*cos((marslng-116.327741)*pi/180)) * 6371004 <= 300
            then 'THU'
         else 'NULL'
         end
        ) univ
     from
        log.mobile_data_location
     where
        dt >= '20131101' and dt <= '20131107'
    ) mdl
where
    mdl.univ != 'NULL'

--
select
    *
from
    (select
        uuid,
        (case 
            when marslat > 39.98714 and marslat < 39.996889 and marslng > 116.304849 and marslng < 116.315235
            then 'PKU'
            when marslat > 30.259491 and marslat < 30.26898 and marslng > 120.122359 and marslng < 120.124891
            then 'ZJU'
            when marslat > 30.632197 and marslat < 30.633397 and marslng > 104.078482 and marslng < 104.083031
            then 'SCU'
            when acos(sin(marslat*pi/180)*sin(40.001137*pi/180) + cos(marslat*pi/180)*cos(40.001137*pi/180)*cos((marslng-116.327741)*pi/180)) * 6371004 <= 300
            then 'THU'
            when acos(sin(marslat*pi/180)*sin(30.541111*pi/180) + cos(marslat*pi/180)*cos(30.541111*pi/180)*cos((marslng-114.361922)*pi/180)) * 6371004 <= 300
            then 'WHU'
            when acos(sin(marslat*pi/180)*sin(31.297978*pi/180) + cos(marslat*pi/180)*cos(31.297978*pi/180)*cos((marslng-121.500632)*pi/180)) * 6371004 <= 300
            then 'FDU'
            when acos(sin(marslat*pi/180)*sin(24.438973*pi/180) + cos(marslat*pi/180)*cos(24.438973*pi/180)*cos((marslng-118.097788)*pi/180)) * 6371004 <= 300
            then 'XMU'
         else 'NULL'
         end
        ) univ,
        dt
    from
        log.mobile_data_location
    where
        dt >= '20131101' and dt <= '20131107'
    group by
        dt, univ
    ) mdl
where
    mdl.univ != 'NULL'