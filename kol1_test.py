#!/usr/bin/env python2

#original code author: github.com/Korfeusz

from __future__ import division
import unittest
import kol1_korfeusz as korfeusz
import math

class test_korfeusz(unittest.TestCase):
    def setUp(self):
        self.environment = korfeusz.Environment(4.7,60)
        self.regulator = korfeusz.Regulator(environment=self.environment, \
            correction_rate=0.5, correct_value=0.0)
    
    def test_environment_creation_wind_strength(self):
        wind_strength = 4.7
        self.assertAlmostEqual(wind_strength, \
            self.environment.wind_strength, places=4)
    
    def test_environment_creation_wind_direction(self):
        wind_direction = 60
        self.assertEqual(wind_direction, self.environment.wind_direction)
            
    def test_environment_correct_angle_conversion(self):
        checked_sine = math.sin(self.environment.wind_direction*math.pi/180.0)
        self.environment.calculate_wind_direction_input_multiplier()
        self.assertAlmostEqual(checked_sine, \
            self.environment.wind_direction_input_multiplier, places=4)
    
    def test_environment_correct_sine(self):
        self.environment()
        random_wind_impact = self.environment.random_wind_impact
        wind_times_sine = self.environment.impact_multiplier
        self.assertGreaterEqual(random_wind_impact, wind_times_sine)
    
    def test_regulator_creation_correction_rate(self):
        correction_rate = 0.5
        self.assertAlmostEqual(correction_rate, \
            self.regulator.correction_rate, places=4)
    
    def test_regulator_creation_correct_value(self):
        correct_value = 0.0
        self.assertAlmostEqual(correct_value, \
            self.regulator.correct_value, places=4)
    
    def test_if_tilt_lowered(self):
        current_tilt = 0.47
        self.environment()
        self.regulator(current_tilt)
        self.assertLessEqual(self.regulator.in_value, current_tilt)

if __name__=='__main__':
    unittest.main()
