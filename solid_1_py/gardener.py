# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:57:23 2019

@author: Ewa
"""


import random


class Gardener:
    NICE_WEATHER_PROBABILITY = 0.75

    def __init__(self, name, gender, fatherName, motherName, dateOfBirth):
        self.name = name
        self.gender = gender
        self.fatherName = fatherName
        self.motherName = motherName
        self.numberOfPlantedTrees = 0
        self.random_generator = random.Random()  # instantiation of rand. gen.
        self.name_of_the_role = 'Gardener'
        self.dateOfBirth = dateOfBirth

    def describe(self):
        return '{0} {1}, {2} of {3} and {4} who was born on {6}, planted {5} trees. '.format(
            self.name_of_the_role,
            self.name, 'son' if self.gender == 'm' else 'daugher',
            self.fatherName, self.motherName, self.numberOfPlantedTrees, self.dateOfBirth)

    def plant(self):
        if self.random_generator.random() < self.NICE_WEATHER_PROBABILITY:
            self.numberOfPlantedTrees += 1
            return 'Planting a tree...'
        return 'Looking at trees growing in the rain...'


def main():
    k = Gardener("Greenleaf", 'm', "Brownleaf",
                 "Goldendaisy", '5th January 1786')
    print(k.describe())
    for i in range(6):
        print(k.plant())


if __name__ == '__main__':
    main()
