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

    def hit_rate(self): 
        hit_val = #program here 
        return hit_val 

    def fl_rate(self): 
        fl_val = #program here 
        return fl_val

    def d_prime(self, hit_val, fl_val): 
        d_val = #Program formula here 
        return d_val 

    def criterion(self, hit_val, fl_val): 
        c_val = #Input formula here 
        return c_val


if __name__ == '__main__': 
    sig_val = SignalDetection