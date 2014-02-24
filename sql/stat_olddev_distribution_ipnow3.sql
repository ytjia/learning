SELECT
    ml.did, ml.ip, ml.net, COUNT(*) cnt
FROM
    (SELECT
        identity
     FROM
        mart_mobile.device_launch_stat
     WHERE
        firstdatekey < 20131107
     ) dls
JOIN
    (SELECT
        did,
        ip,
        net,
        tm
     FROM
        log.mobilelog
     WHERE
        dt = '20131107'
     distribute by did
     sort by did, tm
     ) ml
ON
    dls.identity != '' AND dls.identity = ml.did
GROUP BY
    ml.did, ml.ip,  ml.net