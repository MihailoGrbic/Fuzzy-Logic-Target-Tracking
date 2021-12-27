import numpy as np

import matplotlib.pyplot as plt

from fuzzy_rules import fuzzy_rules


class FuzzyTracker():
    def __init__(self, position=[0.0, 0.0]):
        self.position = np.array(position)
        self.absolute_speed = np.array([0.0, 0.0])
        self.prev_distance = np.array([0.0, 0.0])

    def updateTrackerPos(self, target_pos):
        distance = target_pos - self.position
        relative_speed = self.prev_distance - distance
        self.prev_distance = distance

        # Fuzzy Control X dim
        x_fuzzy_dist = fuzzify_distance(distance[0])
        x_fuzzy_speed = fuzzify_speed(relative_speed[0])
        x_fuzzy_acc = fuzzy_rules(x_fuzzy_dist, x_fuzzy_speed, fuzzy_acceleration())
        x_acc = deffuzify(x_fuzzy_acc)

        # Fuzzy Control Y dim
        y_fuzzy_dist = fuzzify_distance(distance[1])
        y_fuzzy_speed = fuzzify_speed(relative_speed[1])
        y_fuzzy_acc = fuzzy_rules(y_fuzzy_dist, y_fuzzy_speed, fuzzy_acceleration())
        y_acc = deffuzify(y_fuzzy_acc)

        self.absolute_speed += 2 * np.array([x_acc, y_acc])
        self.position += self.absolute_speed

        # print()
        # print(relative_speed)
        # print(distance)
        # print(x_fuzzy_dist)
        # print([x_acc, y_acc])

        # self.position += [1, 0]
        return self.position


def fuzzify_distance(crisp_value):
    fuzzy_dist = {
        'very negative': trapezoid(-10e5, -10e5, -200, -100)(crisp_value),
        'little negative': trapezoid(-200, -100, -10, 0)(crisp_value),
        'zero': trapezoid(-10, 0, 0, 10)(crisp_value),
        'little positive': trapezoid(0, 10, 100, 200)(crisp_value),
        'very positive': trapezoid(100, 200, 10e5, 10e5)(crisp_value),
    }
    return fuzzy_dist


def fuzzify_speed(crisp_value):
    fuzzy_speed = {
        'very negative': trapezoid(-10e2, -10e2, -4, -3)(crisp_value),
        'little negative': trapezoid(-4, -3, -0.5, 0)(crisp_value),
        'zero': trapezoid(-0.5, 0, 0, 0.5)(crisp_value),
        'little positive': trapezoid(0, 0.5, 3, 4)(crisp_value),
        'very positive': trapezoid(3, 4, 10e2, 10e2)(crisp_value),
    }
    return fuzzy_speed


def fuzzy_acceleration():
    fuzzy_acc = {
        'very negative': trapezoid(-0.75, -0.5, -0.5, -0.25),
        'little negative': trapezoid(-0.5, -0.25, -0.25, 0),
        'zero': trapezoid(-0.25, 0, 0, 0.25),
        'little positive': trapezoid(0, 0.25, 0.25, 0.5),
        'very positive': trapezoid(0.25, 0.5, 0.5, 0.75),
    }
    return fuzzy_acc


def deffuzify(aggregate_func, def_type="cog"):
    x = np.linspace(-2, 2, num=10000)
    y = aggregate_func(x)

    if def_type == "meom":
        max_val = max(y)
        mask = y == max_val
        return np.average(x, weights=mask)

    if def_type == "cog":
        return np.average(x, weights=y)


def trapezoid(p1, p2, p3, p4, h=1):
    if p2 == p1:
        p2 += 10e-5
    if p4 == p3:
        p4 += 10e-5

    def trapezoid_func(x):
        return np.minimum(cutoff((x - p1) * h / (p2 - p1)), cutoff((p4 - x) * h / (p4 - p3)))
    return trapezoid_func


def cutoff(value):
    # Forces a value to be between 0 and 1
    return np.minimum(1, np.maximum(0, value))
