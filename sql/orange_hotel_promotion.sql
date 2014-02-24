-- @author: jiayitian
-- @date:   2014/01/13

-- 指定时间内浏览过城市X酒店类订单的本地用户
SELECT
    tt.userid,
    tt.cityid scancityid,
    uri.cityid regcityid
FROM
(
    SELECT
        dvd.userid,
        dvd.cityid,
        dvd.dealid as vdealid,
        deal.dealid as dealid
    FROM
    (
        SELECT
            userid,
            cityid,
            dealid
        FROM
            mart_mobile.deal_visit_daily
        WHERE
            dt BETWEEN '20131201' AND '20140112'
        ) dvd
    JOIN
    (
        SELECT
            dealid
        FROM
            dim.deal
        WHERE
            classid = 209 AND market_cityid = 10
        ) deal
    ON
        dvd.dealid = deal.dealid
) tt
JOIN
(
    SELECT
        userid,
        cityid
    FROM
        dim.userreginfo   
    WHERE
        cityid = 10
    ) uri
ON
    tt.userid = uri.userid

--  指定时间内购买过城市X酒店类订单的用户
SELECT
    tt.userid,
    uri.cityid regcityid
FROM
(   
    SELECT
        usc.userid
        usc.dealid
    FROM
    (
        SELECT
            userid,
            CAST(dealid as INT) dealid
        FROM
            detail.usersequence_client
        WHERE
            datekey BETWEEN 20131229 AND 20140112
        ) usc
    JOIN
    (
        SELECT
            CAST(dealid as INT) dealid
        FROM
            dim.deal
        WHERE
            classid = 209 AND market_cityid = 10
        ) deal
    ON
        usc.dealid = deal.dealid
) tt
JOIN
(
    SELECT
        userid,
        cityid
    FROM
        dim.userreginfo   
    WHERE
        cityid = 10
    ) uri
ON
    tt.userid = uri.userid
