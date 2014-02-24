SELECT
    net, 
    COUNT(*) AS all_dev, 
    sum(case when dls.is_fraud = 1
        then 1 else 0 end) as fraud_dev,
FROM
    (SELECT
        identity,
        (case when secondkeydate = 0
         then 1 else 0 end) as is_fraud
     FROM
        mart_mobile.device_launch_stat
     WHERE
        firstdatekey BETWEEN 20131106 AND 20131108
     ) as dls
    JOIN
    (SELECT
        *
     FROM
     (
        SELECT
            did,
            ct,
            os,
            app,
            net,
            tm
        FROM
            log.mobilelog
        WHERE
            dt BETWEEN 20131106 AND 20131108
        distribute by did
        sort by did, tm
      ) t
     ) as ml
on
    dls.identity = ml.did
GROUP BY
    ml.ct, ml.app
