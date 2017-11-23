import unittest
from kol1_korfeusz import Environment, Regulator
#import numpy as np

class test_korfeusz(unittest.TestCase):
	def setUp(self):
		self.environment = Environment(4.7,60)
		self.regulator = Regulator(environment=self.environment, \
			correction_rate=0.5, correct_value=0.0)
	
	def test_check_if_tilt_corrected(self):
		current_tilt = 0.47
		environment()
        tilt_regulator(current_tilt)
        self.assertLess(tilt_regulator,current_tilt)

if __name__=='__main__':
	unittest.main()
