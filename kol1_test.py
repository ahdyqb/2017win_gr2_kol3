#!/usr/bin/env python2

#original code author: github.com/Korfeusz

from __future__ import division
import unittest
from kol1_korfeusz import Environment, Regulator
import math

class test_korfeusz(unittest.TestCase):
	def setUp(self):
		self.environment = Environment(4.7,60)
		self.regulator = Regulator(environment=self.environment, \
			correction_rate=0.5, correct_value=0.0)
			
	def test_check_if_correct_angle_conversion(self):
		checked_sine = math.sin(self.environment.wind_direction*math.pi/180.0)
		self.environment.calculate_wind_direction_input_multiplier()
		self.assertAlmostEqual(checked_sine, self.environment.random_wind_impact, places=4)
	
	def test_check_if_tilt_corrected(self):
		current_tilt = 0.47
		environment()
        self.regulator(current_tilt)
        self.assertLess(self.regulator,current_tilt)

if __name__=='__main__':
	unittest.main()
