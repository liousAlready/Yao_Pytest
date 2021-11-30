# -*- coding: utf-8 -*-
# @Time : 2021/11/15 13:43
# @Author : Limusen
# @File : random_utils

import random
from Common.log_utils import logger


class RandomUtils:

    def Rphone(self):
        segment = ['130', '136', '138', '137', '150', '155', '158', '177', '186', '185']
        phone = random.choice(segment) + "".join(random.choice("0123456789") for i in range(8))
        logger.info("当前正在打印手机号码: %s" % phone)
        return phone

    def Rcode(self):
        code = ''.join(random.choice("0123456789") for i in range(5))
        logger.info("当前正在打印code: %s" % code)
        return code

    def Rname(self):
        surname = ["赵", "钱", "孙", "李", "欧阳", "武", "毛", "刘", "方", "邱"]
        name = random.choice(surname) + "".join(random.choice("祺禄祥玺嘉霖麒麟") for i in range(2))
        logger.info("当前正在打印名字: %s" % name)
        return name


rd = RandomUtils()

if __name__ == '__main__':
    # name = RandomUtils().Rname()
    name = rd.Rcode()
    print(name)
