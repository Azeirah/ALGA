"""Implements an enemy (WEIGHT) for the dungeon"""


class Enemy():
    def __init__(self, room, hp):
        self.room = room
        self.hp = hp
        print("I am an enemy with {hp}hp".format(hp=self.hp))

    def cellType(self):
        return str(self.hp)
