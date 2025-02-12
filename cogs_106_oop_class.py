import math 
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm

"""
Goal: Create a class that implements the signal-detection-theory formulas. 

Structure: 
- d_prime:  Returns the d-prime value given the hit rate and false alarm rate.
- criterion: Returns the criterion value given the hit rate and false alarm rate.
- IMPORTANT NOTE: d_prime and criterion rely on the Hit rate and false alarm rate to compute their respective values 
    - Create two methods that calculate and return the hit rate and the false alarm rate before integrating those 
    values into d_prime and criterion.
    - however, start by coding the methods for d_prime and criterion first and work backwards. 
"""

class SignalDetection: 

    def __init__(self, hits, misses, falseAlarms, correctRejections): 
        self.hits = hits 
        self.misses = misses
        self.falseAlarms = falseAlarms 
        self.correctRejections = correctRejections 

    def hit_rate(self, hits, misses): 
        """Calculates the proportion of identified signal trials. Returns string when denominator == 0"""
        return hits/(hits + misses) if (hits + misses) > 0 else "Error"
    
    def fl_rate(self, falseAlarms, correctRejections): 
        """Calculates the proportion of noise trials that were incorrectly detected. Returns string when denominator == 0"""
        return falseAlarms/(falseAlarms + correctRejections) if (falseAlarms + correctRejections) > 0 else "Error"

    def d_prime(self): 
        """returns difference between the standard deviations of hit rate and false alarm rate."""
        d_val = norm.ppf(self.hit_rate) - norm.ppf(self.fl_rate)
        return d_val 

    def criterion(self): 
        """Returns response bias times the sum of the standard devations of hit rate and false alarm rate"""
        c_val = -0.5 * (norm.ppf(self.hit_rate) + norm.ppf(self.fl_rate))
        return c_val
    
#Example usage 

sd = SignalDetection(15, 5, 15, 5)
hit_result = sd.hit_rate 
print(hit_result) 

sd = SignalDetection(15, 5, 15, 5)
fl_result = sd.fl_rate
print(fl_result) 
