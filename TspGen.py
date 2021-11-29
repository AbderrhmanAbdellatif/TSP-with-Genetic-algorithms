# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 20:44:26 2021

@author: aellatif
"""

"""
    Provided with the initial population first we apply a fitness function
    which will be the division of the tour distance divided by the best distance
    we have after each iteration. Then we apply a roulette-wheel selection on the population
    to get from the accumulated fitness of each tour a random pick
"""

from operator import itemgetter
import random
import collections
import copy




class TSPGeneticAlgo:
    def __init__(self):
        self.groups_of_two = []
    def create_mutation(self,poplist): # 0.1 0.2 0.3 ... 0.10
        poplistsize=len(poplist)
        mutation_operator_list=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,0.10]
        mutation_operator_size = random.choice(mutation_operator_list)  # for 0.1 0.2 0.3 0.3 ......
        mutsize = int(poplistsize * mutation_operator_size) # 101 * 0.1 = 10
        for i in range(mutsize):  # randomly chosee mut
            index = random.randint(0, len(poplist_size) - 1)
            poplist[index] = self.insertion_mutation(poplist[index]).copy()

    def insertion_mutation(self,in_list):
        tour_range = len(in_list)
        randominsert = random.randint(0, tour_range - 1)
        randomip = random.randint(0, tour_range - 1)
        city_to_insert = in_list.pop(randomip)
        in_list.insert(randominsert, city_to_insert)
        return in_list
    def crossover(self, parent1, parent2):
        def process_gen_repeated(copy_child1, copy_child2):
            count1 = 0
            for gen1 in copy_child1[:pos]:
                repeat = 0
                repeat = copy_child1.count(gen1)
                if repeat > 1:  # If need to fix repeated gen
                    count2 = 0
                    for gen2 in parent1[pos:]:  # Choose next available gen
                        if gen2 not in copy_child1:
                            child1[count1] = parent1[pos:][count2]
                        count2 += 1
                count1 += 1

            count1 = 0
            for gen1 in copy_child2[:pos]:
                repeat = 0
                repeat = copy_child2.count(gen1)
                if repeat > 1:  # If need to fix repeated gen
                    count2 = 0
                    for gen2 in parent2[pos:]:  # Choose next available gen
                        if gen2 not in copy_child2:
                            child2[count1] = parent2[pos:][count2]
                        count2 += 1
                count1 += 1
            return [child1, child2]

        pos = random.randrange(1, 101-1)
        child1 = parent1[:pos] + parent2[pos:]
        child2 = parent2[:pos] + parent1[pos:]

        return process_gen_repeated(child1, child2)


