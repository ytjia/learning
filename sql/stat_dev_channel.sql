SELECT
    dinfo.adsourcelinkid,
    dls.firstdatekey,
    dls.lastdatekey,
    dinfo.identity
    FROM
    (SELECT
        identity,
        firstdatekey,
        lastdatekey
     FROM
        mart_mobile.device_launch_stat
     WHERE
        firstdatekey BETWEEN 20131101 AND 20131107
    ) dls
JOIN
    (SELECT
        identity,
        adsourcelinkid
     FROM
        dim.deviceinfo
     WHERE
        firstdate BETWEEN '20131101' AND '20131107'
    ) dinfo
ON
    dls.identity = dinfo.identity

-- 
SELECT
    dls.identity,
    dls.firstdatekey,
    dls.seconddatekey,
    mi.adsourcelinkid
FROM
    (SELECT
        *
     FROM
        mart_mobile.device_launch_stat
     WHERE
        firstdatekey BETWEEN 20131201 AND 20131207
        AND
        (seconddatekey - firstdatekey > 7
        OR
        seconddatekey = 0)
     ) dls
JOIN
    (SELECT
        identity,
        adsourcelinkid
     FROM
        dim.mobileinfo
     WHERE
        firstdate BETWEEN '2013-12-01' AND '2013-12-07'
     ) mi
ON
    dls.identity = mi.identity
        
