class TempTracker(object):
    def __init__(self):
        self.max_temp = 0
        self.min_temp = 110
        self.running_temp_total = 0
        self.total_temps = 0
        self.temp_count = [0] * 111
        self.mode_index = 0

    def insert(self, temp):
        self.max_temp = max(self.max_temp, temp)
        self.min_temp = min(self.min_temp, temp)
        self.running_temp_total += temp
        self.total_temps += 1
        self.temp_count[temp] += 1
        if self.temp_count[temp] > self.temp_count[self.mode_index]:
            self.mode_index = temp

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        if self.total_temps == 0:
            return None

        return float(self.running_temp_total) / self.total_temps

    def get_mode(self):
        return self.mode_index

    def __str__(self):
        return "max: %s; min: %s; mean: %s; mode: %s" % (self.get_max(), self.get_min(), self.get_mean(), self.get_mode())

tracker = TempTracker()

tracker.insert(5)
print tracker

tracker.insert(4)
print tracker

tracker.insert(99)
print tracker

tracker.insert(99)
print tracker

tracker.insert(50)
print tracker

tracker.insert(50)
print tracker

tracker.insert(99)
print tracker

tracker.insert(34)
print tracker

