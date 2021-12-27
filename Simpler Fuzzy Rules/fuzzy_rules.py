import numpy as np


def fuzzy_rules(f_dist, f_spd, f_acc):
    rules = [
        #    impl(f_dist['very negative'],
        #         f_acc['very negative']),
        impl(f_and(f_dist['very negative'], f_spd['very negative']),
             f_acc['little negative']),
        impl(f_and(f_dist['very negative'], f_not(f_spd['very negative'])),
             f_acc['very negative']),

        impl(f_and(f_dist['little negative'], f_spd['very negative']),
             f_acc['little positive']),
        impl(f_and(f_dist['little negative'], f_spd['little negative']),
             f_acc['zero']),
        impl(f_and(f_dist['little negative'], f_spd['zero']),
             f_acc['little negative']),
        impl(f_and(f_dist['little negative'], f_or(f_spd['little positive'], f_spd['very positive'])),
             f_acc['very negative']),

        impl(f_and(f_dist['zero'], f_spd['very negative']),
             f_acc['very positive']),
        impl(f_and(f_dist['zero'], f_spd['little negative']),
             f_acc['little positive']),
        impl(f_and(f_dist['zero'], f_spd['zero']),
             f_acc['zero']),
        impl(f_and(f_dist['zero'], f_spd['little positive']),
             f_acc['little negative']),
        impl(f_and(f_dist['zero'], f_spd['very positive']),
             f_acc['very negative']),

        impl(f_and(f_dist['little positive'], f_or(f_spd['little negative'], f_spd['very negative'])),
             f_acc['very positive']),
        impl(f_and(f_dist['little positive'], f_spd['zero']),
             f_acc['little positive']),
        impl(f_and(f_dist['little positive'], f_spd['little positive']),
             f_acc['zero']),
        impl(f_and(f_dist['little positive'], f_spd['very positive']),
             f_acc['little negative']),

        impl(f_and(f_dist['very positive'], f_spd['very positive']),
             f_acc['little positive']),
        impl(f_and(f_dist['very positive'], f_not(f_spd['very positive'])),
             f_acc['very positive']),
    ]

    def aggregate_func(x):
        maxx = 0
        for func in rules:
            maxx = np.maximum(func(x), maxx)
        return maxx

    return aggregate_func


def impl(left_val, right_func, implication_type='min'):
    def func(x):
        if implication_type == 'min':
            return np.minimum(left_val, right_func(x))
        if implication_type == 'mul':
            return left_val * right_func(x)

    return func


def f_and(a, b, op_type='zadeh'):
    if op_type == 'zadeh':
        return np.minimum(a, b)
    if op_type == 'probabilistic':
        return a * b


def f_or(a, b, op_type='zadeh'):
    if op_type == 'zadeh':
        return np.maximum(a, b)
    if op_type == 'probabilistic':
        return a + b - a * b


def f_not(a):
    return 1 - a
