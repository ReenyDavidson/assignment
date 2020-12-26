# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 09:57:12 2019

@author: Ewa
"""


class Knight:
    def __init__(self, name, gender, fatherName, motherName, weapon, mount, dateOfBirth, newRole):
        self.name = name
        self.gender = gender
        self.fatherName = fatherName
        self.motherName = motherName
        self.weapon = weapon
        self.mount = mount
        self.strength = 1
        self.name_of_the_role = 'Knight'
        self.dateOfBirth = dateOfBirth
        self.newRole = newRole

    def describe(self):
        return ' {0} {1}, {2} of {3} and {4} who was born on {7}, fights using a {5} rides on a {6}. '.format(
            self.name_of_the_role,
            self.name, 'son' if self.gender == 'm' else 'daugher',
            self.fatherName, self.motherName,  self.weapon, self.mount,
            self.dateOfBirth, 'Can fight' if self.strength > 0 else 'Needs a rest')

    def fight(self):
        if self.strength <= 0:
            self.strength = 1.0
            return 'Resting...'
        self.strength -= 0.25
        return 'Figting...'

    def castASpell(self):
        return '{} the {} casted a spell: Abracadabra!'.format(self.name, self.newRole)


def main():
    k = Knight('Quickhand', 'm', 'Bravedeed', 'Sunbell', 'sword',
               'horse', '5th January 1786', 'Wizard')
    print(k.describe())
    for i in range(6):
        print(k.fight())
    print(k.castASpell())


if __name__ == '__main__':
    main()
