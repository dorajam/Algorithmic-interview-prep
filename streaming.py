import numpy as np

class StreamingMean(object):
    
    def __init__(self):
        self.total_num = 0
        self.total_sum = 0

    def insert(self, new_measures):
        self.total_num += len(new_measures)
        self.total_sum += sum(new_measures)

    def get_current_mean(self):
        if self.total_num != 0:
            return float(self.total_sum) / self.total_num
        return np.nan
