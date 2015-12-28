# -*- coding: utf-8 -*-
# !usr/bin/env python

"""
    @author : ginxd
    @contact : ginxdxd@gmail.com
    @file : GBDT.py
    @time : 24/12/15
"""

"""
    默认data_set最后一列为target
"""

import numpy as np

def main():
    test = [[1,2,3], [4,5,6], [2,2,3]]
    task = np.array(test)

    mat = task[[0, 2], :]
    print mat

def GBDT(data_set):
    value = set(data_set[:, -1])
    if len(value) == 1:
        return list(value)[0]
    if len(data_set) == 1:
        return np.mean(data_set)

    tree = {}
    fir_feature = get_best_feature(data_set)


def get_best_feature(data_set):
    n_features = data_set.shape[1]
    # for i in range(n_features):



if __name__ == '__main__':
    main()