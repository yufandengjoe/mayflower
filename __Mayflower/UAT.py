# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 09:45:27 2022

@author: yufan
"""


class cal:

    def __init__(self, yield_) -> None:
        self.yield_ = yield_

    def cal_2(self):
        if not hasattr(self.yield_, '__call__'):
            print(0)
            return None
        else:
            for i in range(5):
                div = self.yield_(i, i+1)
                print(div)
            return None


cal_obj = cal(max)
print(cal_obj.yield_(1, 2))
cal_obj.cal_2()
