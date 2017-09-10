#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
################################################################################
#
# Copyright (c) 2017 gusong.org All Rights Reserved
#
################################################################################
"""
This module: provide round-robin scheduling and weighted round-robin scheduling
 Date 2017/09/10 22:15:06
 Author andy(gusong)
"""
import sys
import time
import json

reload(sys)
sys.setdefaultencoding('utf-8')

N = 3 # count
WEIGTH = (60, 30, 10)

# RR
def rr_select():
    """ Round-Robin Scheduling, get elements from each queue orderly
        N: number of the queues
        0 ~ N - 1: the seq of these queues
    """
    last = N - 1
    while True:
        current = (last + 1) % N
        last = current
        yield current

# WRR
def gcd(nums):
    """ get the greatest common divisor of the nums
    """
    m = nums[0]
    for n in nums[1:]:
        while n != 0:
            m, n = n, m % n
    return m


def wrr_select():
    """Weighted Round-Robin Scheduling
       current_weight     pick element from which queue
       60                 0
       50                 0
       40                 0
       30                 0 1
       20                 0 1
       10                 0 1 2
    """
    current = N - 1
    current_weight = 0

    while True:
        current = (current + 1) % N
        if current == 0:
            current_weight -= gcd(WEIGTH)
            if current_weight <= 0:
                current_weight = max(WEIGTH)
        if WEIGTH[current] >= current_weight:
            yield current


if __name__ == "__main__":
    rr_sample = rr_select()
    print "-------RR:"
    for i in xrange(20):
        print rr_sample.next()

    print "-------WRR:"
    wrr_sample = wrr_select()
    for i in xrange(20):
        print wrr_sample.next()
