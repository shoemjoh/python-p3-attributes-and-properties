#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    approved_jobs = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

    def __init__(self, name="Person", job="General Management"):
        self.name = name  # Calls the setter method for validation and title case
        self.job = job  # Calls the setter method for validation

    # Getter for name
    def get_name(self):
        return self._name

    # Setter for name with validation and conversion to title case
    def set_name(self, name):
        if isinstance(name, str) and (0 < len(name) <= 25):
            self._name = name.title()  # Convert name to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    # Getter for job
    def get_job(self):
        return self._job

    # Setter for job with validation against the approved list
    def set_job(self, job):
        if job in self.approved_jobs:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")

    # Define properties
    name = property(get_name, set_name)
    job = property(get_job, set_job)

