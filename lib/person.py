#!/usr/bin/env python3

APPROVED_JOBS = [
    "Sales",
    "Engineer",
    "Manager",
    "Artist",
    "Chef",
    "Doctor",
    "Programmer",
    "ITC"
]

class Person:
    def __init__(self, name=None, job=None):
        self._name = None
        self._job = None
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value is None:
            return
        if not isinstance(value, str) or len(value) < 1 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value is None:
            return
        if value not in APPROVED_JOBS:
            print("Job must be in list of approved jobs.")
        else:
            self._job = value
