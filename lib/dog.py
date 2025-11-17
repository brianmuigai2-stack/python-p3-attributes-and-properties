#!/usr/bin/env python3

from operator import length_hint


APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name=None, breed=None):
        self.name = None
        self.breed = breed
        self.set_name(name)
        self.set_breed(breed)

    def set_name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self.name = name
        else:
            if name is not None:
              print("Name must be string between 1 and 25 characters.")

    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            self.breed = breed
        else:
            if breed is not None:
              print("Breed must be in list of approved breeds.")
     
