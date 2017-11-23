###Flight simulator.
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth).
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations").
#With every simulation step the orentation should be corrected, applied and printed out.
#If you can thing of any other features, you can add them.
#This code shoud be runnable with 'python kol1.py'.
#If you have spare time you can implement: Command Line Interface, generators, or even multiprocessing.
#Do your best, show off with good, clean, well structured code - this is more important than number of features.
#After you finish, be sure to UPLOAD this (add, commit, push) to the remote repository.
#Good Luck
import numpy as np
import time
class Environment:
    def __init__(self, wind_strength=5, wind_direction=90):
        self.wind_strength = wind_strength
        self.wind_direction = wind_direction

    def calculate_wind_direction_input_multiplier(self):
        self.wind_direction_input_multiplier = np.abs(np.sin(np.deg2rad(self.wind_direction)))

    def calculate_random_wind_impact(self):
        self.random_wind_impact = np.random.normal() * self.wind_strength

    def calculate_environment_multiplier(self):
        self.impact_multiplier = self.random_wind_impact * self.wind_direction_input_multiplier

    def __call__(self):
        self.calculate_wind_direction_input_multiplier()
        self.calculate_random_wind_impact()
        self.calculate_environment_multiplier()

    def __str__(self):
        return str(self.impact_multiplier)


class Regulator:
    def __init__(self, environment, correction_rate=0.1, correct_value=0):
        self.correction_rate = correction_rate
        self.correct_value = correct_value
        self.environment = environment

    def _regulate(self):
        correction =  np.sign(self.in_value) * self.correction_rate * self.error_impact
        self.new_value = self.correct_value + correction

    def _calculate_error_impact(self):
        error = np.abs(self.in_value - self.correct_value)
        environment_multiplier = self.environment.impact_multiplier
        self.error_impact = environment_multiplier * error

    def __call__(self, in_value):
        self.in_value = in_value
        self._calculate_error_impact()
        self._regulate()

    def __str__(self):
        return str(self.new_value)


if __name__ == "__main__":
    print "Press Ctrl-c to exit"

    environment = Environment()
    tilt_regulator = Regulator(correct_value = 0.5, environment=environment)

    while True:
        current_tilt = np.random.normal()
        environment()
        tilt_regulator(current_tilt)
        print "tilt was: {} corrected to: {}".format(current_tilt, tilt_regulator)
        time.sleep(1)

