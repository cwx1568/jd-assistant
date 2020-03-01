#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    # asst.clear_cart()
    # asst.add_item_to_cart(sku_ids='32275966268')
    # asst.submit_order()
    asst.submit_order_by_time(buy_time='2019-12-12 10:16:59.500', retry=10000, interval=5)

    # asst.submit_order_by_stock(sku_ids='32275966268', area='2_2824_51917_0')

    # asst.exec_reserve_seckill_by_time(sku_id="32275966272", buy_time="2019-11-10 22:42:30.000")
    # 执行预约抢购
    # 5个参数
    # sku_id: 商品id
    # buy_time: 下单时间，例如：'2019-11-10 22:41:30.000'
    # retry: 抢购重复执行次数，可选参数，默认4次
    # interval: 抢购执行间隔，可选参数，默认4秒
    # num: 购买数量，可选参数，默认1个
