select
    ml.net,
    ml.ip,
    count(*) all_dev,
    sum(case when dls.is_fraud = 1
        then 1 else 0 end) fraud_dev
from
    (select
        identity,
        (case when seconddatekey = 0
         then 1 else 0 end) is_fraud
     from
        mart_mobile.device_launch_stat
     where
        firstdatekey between 20131106 and 20131108
    ) dls
join
    (select
        did,
        net,
        ip,
        tm
     from
        log.mobilelog
     where
        dt between '20131106' and '20131108'
     distribute by did
     sort by did, tm
    ) ml
on
    dls.identity = ml.did
group by
    ml.net, ml.ip
