# -*- coding: utf-8 -*-

"""
春运发券数据统计
"""
def filter_cond():
    fcoupon = open(r'/Users/ytjia/Downloads/20w发券用户')
    fconsume = open(r'/Users/ytjia/Downloads/period_consume')
    fcouponbuy = open(r'/Users/ytjia/Downloads/consumed_coupon', 'w')
    fnormalbuy = open(r'/Users/ytjia/Downloads/consumed_normal', 'w')
    all_usr = set()
    coupon_usr = set()
    coupon_buy = set()
    normal_buy = set()

    user_file = ['user_5.8w', 'user_25w', 'user_35w']
    for file_name in user_file:
        finput = open(r'/Users/ytjia/Downloads/65W用户分三组/%s' % file_name)
        for line in finput.readlines():
            record = line.split()
            all_usr.add(record[0])
        finput.close()
    for line in fcoupon.readlines():
        record = line.split()
        coupon_usr.add(record[0])
    for line in fconsume.readlines():
        record = line.split()
        if record[0] in coupon_usr:
            coupon_buy.add(record[0])   # 去重
        elif record[0] in all_usr:
            normal_buy.add(record[0])
    for userid in coupon_buy:
        fcouponbuy.write(userid + '\n')
    for userid in normal_buy:
        fnormalbuy.write(userid + '\n')
    fcoupon.close()
    fconsume.close()
    fcouponbuy.close()
    fnormalbuy.close()

if __name__ == '__main__':
    filter_cond()