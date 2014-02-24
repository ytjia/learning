ELECT
    ml.did, 
    ml.dm,
    mi.adsourcelinkid,
    ml.dt
FROM
    (SELECT
        *
     FROM
      (SELECT
          did,
          dm,
          dt
       FROM
          log.mobilelog
       WHERE
          dt BETWEEN '20131101' AND '20131107' 
       AND dm != ''
       distribute by did
       sort by did
       ) t
     WHERE
        mtrank(did) = 0
     ) ml
JOIN
    (SELECT
        identity,
        adsourcelinkid
     FROM
        dim.mobileinfo
     WHERE
        firstdate BETWEEN '2013-11-01' AND '2013-11-07'
     ) mi
ON
    ml.did = mi.identity
