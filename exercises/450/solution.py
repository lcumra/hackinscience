# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:09:48 2015

@author: pippo
"""
import string
import checker
al = list(string.ascii_lowercase)


def caesar_cypher(s, k, m):
    code = list(s)
    ori = list(s)
    resu = list(s)
    for i in range(0, len(s)):
        if checker.numa(ori[i]) != 666:
            code[i] = checker.numa(ori[i])
            if m == "backward":
                code[i] = (code[i] - k) % 26
            if m == "forward":
                code[i] = (code[i] + k) % 26
                resu[i] = al[code[i]]
        else:
            resu[i] = ori [i]
    return resu
