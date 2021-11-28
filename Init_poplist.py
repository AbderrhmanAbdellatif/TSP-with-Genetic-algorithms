# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 21:32:39 2021

@author: aellatif
"""

import numpy as np
import random
from TspDistance import *

class TSPInitialPopulation:
    def __init__(self, cities_dict, init_tour, pop_size):
        self.shuffle_population = 0
        self.pop_group = []  # this is the entire population produced
        self.init_tour = init_tour  # the initial tour provided [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100...
        self.cities_dict = cities_dict  # the dictionary with city:coordinates {1: ('41', '49'), 2: ('35', '17'), 3: ('55', '45'), 4: ('55', '20'), 5: ('15', '30'), 6: ('25', '30'), 7: ('20', '50'), 8: ('10', '43'), 9: ('55', '60'), 10: ('30', '60'), 11: ('20', '65'), 12: ('50', '35'), 13: ('30', '25'), 14: ('15', '10'), 15: ('30', '5'), 16: ('10', '20'), 17: ('5', '30'), 18: ('20', '40'), 19: ('15', '60'), 20: ('45', '65'), 21: ('45', '20'), 22: ('45', '10'), 23: ('55', '5'), 24: ('65', '35'), 25: ('65', '20'), 26: ('45', '30'), 27: ('35', '40'), 28: ('41', '37'), 29: ('64', '42'), 30: ('40', '60'), 31: ('31', '52'), 32: ('35', '69'), 33: ('53', '52'), 34: ('65', '55'), 35: ('63', '65'), 36: ('2', '60'), 37: ('20', '20'), 38: ('5', '5'), 39: ('60', '12'), 40: ('40', '25'), 41: ('42', '7'), 42: ('24', '12'), 43: ('23', '3'), 44: ('11', '14'), 45: ('6', '38'), 46: ('2', '48'), 47: ('8', '56'), 48: ('13', '52'), 49: ('6', '68'), 50: ('47', '47'), 51: ('49', '58'), 52: ('27', '43'), 53: ('37', '31'), 54: ('57', '29'), 55: ('63', '23'), 56: ('53', '12'), 57: ('32', '12'), 58: ('36', '26'), 59: ('21', '24'), 60: ('17', '34'), 61: ('12', '24'), 62: ('24', '58'), 63: ('27', '69'), 64: ('15', '77'), 65: ('62', '77'), 66: ('49', '73'), 67: ('67', '5'), 68: ('56', '39'), 69: ('37', '47'), 70: ('37', '56'), 71: ('57', '68'), 72: ('47', '16'), 73: ('44', '17'), 74: ('46', '13'), 75: ('49', '11'), 76: ('49', '42'), 77: ('53', '43'), 78: ('61', '52'), 79: ('57', '48'), 80: ('56', '37'), 81: ('55', '54'), 82: ('15', '47'), 83: ('14', '37'), 84: ('11', '31'), 85: ('16', '22'), 86: ('4', '18'), 87: ('28', '18'), 88: ('26', '52'), 89: ('26', '35'), 90: ('31', '67'), 91: ('15', '19'), 92: ('22', '22'), 93: ('18', '24'), 94: ('26', '27'), 95: ('25', '24'), 96: ('22', '27'), 97: ('25', '21'), 98: ('19', '21'), 99: ('20', '26'), 100: ('18', '18'...
        self.pop_size = pop_size  # the initial amount of population that will be created 100
        self.random_remaining_cities = self.init_tour[:]  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100...
        self.random_cities = []
        self.create_the_initial_population()

    def create_the_initial_population(self):
        self.shuffle_population = self.pop_size  # 100
        self.shuffle_list(self.init_tour, self.shuffle_population)

    def shuffle_list(self, tour_list, pop_size):
        """
            We create a numpy array and we use permutation
            to create different arrays equal to the size of
            initial population
        """
        x = np.array(tour_list)  # x:[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100...]
        while len(self.pop_group) < self.shuffle_population:  # we start the solution with 100 steps , we give 100 random arrays  and add self.pop_group
            y = np.random.permutation(x)
            if not any((y == x).all() for x in
                       self.pop_group):  # contions if same array x is mean cties tors is not equal  generta array "y"
                self.pop_group.append(y.tolist())  # then add to to  soltion steps

    def find_nn(self, city, list):
        """
            Given a city we find the next nearest city
        """
        start_city = self.get_coordinates_from_city(city)
        return min((euclidean_distance(start_city, self.get_coordinates_from_city(rest)), rest) for rest in
                   list)

    def get_coordinates_from_city(self, city):
        """
            Given a city return the coordinates (x,y)
        """
        return self.cities_dict.get(city)

    def pick_random_city(self):
        """
            Random pick of a city. Persist of uniqueness each time
            the city is added to the random city list and removed
            from remaining cities. Each time we pick a new one from
            the eliminated list of remaining cities
        """
        if self.random_remaining_cities:
            self.random_city = random.choice(self.random_remaining_cities)
            self.random_remaining_cities.remove(self.random_city)
            self.random_cities.append(self.random_city)
        return self.random_city

    def create_nearest_tour(self, city):
        prov_list = self.init_tour[:]
        nearest_tour = [city]
        if city in prov_list: prov_list.remove(city)
        while prov_list:
            current_city = nearest_tour[-1]
            next_city = self.find_nn(current_city, prov_list)
            nearest_tour.append(next_city[1])
            prov_list.remove(next_city[1])
        self.elitism_group.append(nearest_tour)

    def population_analysis(self):
        tour_population = len(self.init_tour)
        if tour_population < self.pop_size / 2:
            self.elitism_population = tour_population
            self.shuffle_population = self.pop_size - self.elitism_population
        else:
            self.elitism_population = self.pop_size / 2
            self.shuffle_population = self.pop_size / 2
    @staticmethod
    def insertion_mutation(in_list):
        tour_range = len(in_list)
        randomip = random.randint(0, tour_range)
        city_to_insert = in_list.pop()
        in_list.insert(randomip, city_to_insert)
        return in_list

    @staticmethod
    def reciprocal_exchange_mutation(in_list):
        a = random.randint(0, len(in_list) - 1)
        b = random.randint(0, len(in_list) - 1)
        in_list[b], in_list[a] = in_list[a], in_list[b]
        return in_list

    @staticmethod
    def inversion_mutation(in_list):
        a = random.randint(0, len(in_list) - 1)
        b = random.randint(0, len(in_list) - 1)
        if a < b:
            a = a
            b = b
        elif a > b:
            a = b
            b = a
        else:
            pass
        first, second, third = in_list[:a], in_list[a:b], in_list[b:]
        in_list = first + second[::-1] + third
        return in_list
