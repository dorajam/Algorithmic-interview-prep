# Dora Jambor
# temptracker.py
# interview cake prep

class TempTracker(object):
    '''Implement the following methods: insert a temperature, get the max, min, mean and mode of all temperatures stored.
    Favor speeding up the latter methods over the insert method'''

    def __init__(self):
        self.max_temp = None
        self.min_temp = None

        self.total_num = 0
        self.total_sum = 0
        self.mean_temp = None

        self.mode_temp = {}
        self.max_occur = 0

    def insert(self, new_temp):
        self.max_temp = max(self.max_temp, new_temp) if self.max_temp != None else new_temp
        self.min_temp = min(self.min_temp, new_temp) if self.min_temp != None else new_temp

        self.total_num += 1
        self.total_sum += new_temp
        self.mean_temp = float(self.total_sum) / self.total_num

        temp_occur = self.mode_temp.get(new_temp, 0)
        if temp_occur!= 0:
            self.mode_temp[new_temp] += 1
        else:
            self.mode_temp[new_temp] = 1
        if temp_occur > self.mode_temp.get(self.max_occur, 0):
            self.max_occur = new_temp

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean_temp

    def get_mode(self):
        return self.max_occur


tt = TempTracker()
tt.insert(34)
tt.insert(21)
tt.insert(76)
tt.insert(76)
print tt.get_max()
print tt.get_min()
print tt.get_mean()
print tt.get_mode()
