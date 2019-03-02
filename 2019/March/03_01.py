# This is your coding interview problem for today.
#
# This problem was asked by Apple.
#
# Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

import time


def job_scheduler(func, n):
    time.sleep(n)
    func()


