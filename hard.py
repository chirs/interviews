



# 18.9
# Numbers are randomly generated and passed to a method. Write a program to find and maintain the median value as new values are generated.

class Median(object):

    def __init__(self):
        self.sum = 0
        self.count = 0


    def push(self, e):
        self.sum += e
        self.count += 1

    def median(self):
        if self.count == 0:
            return None
        else:
            return 1.0 * self.sum / self.count
