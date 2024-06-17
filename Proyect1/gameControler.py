import time
import numpy as np
from Settings import *

class GameControler:
    def __init__(self):
        self.pre_time = self.current_time = time.time()
        self.state = -1

    def update_state(self, num_persons):

        num_persons = min(num_persons, want_person + 1)
        num_persons = max(num_persons, want_person)

        if num_persons == self.state:
            self.current_time = time.time()
        else:
            self.pre_time = self.current_time = time.time()

        self.state = num_persons

    def alert(self):
        if self.state == 1:
            return False
        dif = self.current_time - self.pre_time

        print("dif: ", dif)

        if dif <= duration_counting:
            return False

        return True
