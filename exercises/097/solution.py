# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 18:56:59 2015

@author: pippo
"""


def love_meet(a, b):
    meet = set()
    alen = len(a)
    for i in range(0, alen):
        if a[i] in b:
            meet.add(a[i])
    return meet


def affair_meet(b, a, c):
    meet = set()
    alen = len(a)
    for i in range(0, alen):
        if a[i] in c and a[i] not in b:
            meet.add(a[i])
    return meet
