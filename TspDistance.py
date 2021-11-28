# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import math


def euclidean_distance(p0, p1):
    """
        Calculates the Euclidean distance between 2 points (x1,y1) and (x2,y2)
    """
    xdiff = float(p1[0]) - float(p0[0])
    ydiff = float(p1[1]) - float(p0[1])
    return int(math.sqrt((xdiff * xdiff + ydiff * ydiff) + 0.5))


class TSPDistance:
    def __init__(self, tourlist, citydict):
        self.cities_best = []
        self.tourlist = tourlist
        self.citydict = citydict
        for i in self.tourlist:
            self.cities_best.append(self.citydict.get(i))# add coor to list like ('41', '49'), ('35', '17'), and take the coor oerader
        self.distance_cost = self.total_distance(self.cities_best)# calaculte distance by using this function euclidean_distance

    def total_distance(self, cities_best):
        """
            Iterates a list of coordinate tuples and calculates the Euclidean
            distance between 2 points found sequential in the list representing
            the tour. Then sums everything up and returns the result
        """
        cities_best = self.cities_best
        return sum(euclidean_distance(v, w) for v, w in zip(cities_best[:-1], cities_best[1:]))