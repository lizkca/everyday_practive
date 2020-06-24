# lift.py
# writen by lizkca

import time

class Lift():

    def __init__(self,v,current_floor):
        self.v = v
        self.current_floor = current_floor

    def get_current_floor(self):
        return self.current_floor

    def set_current_floor(self, n):
        self.current_floor = n

    def goto_n_floor(self, n):
        t = (n - self.current_floor) * self.v
        time.sleep(t)
        self.set_current_floor(n)



if __name__ == '__main__':
    my_lift = Lift(2,1)
    my_lift.goto_n_floor(10)
    print(my_lift.get_current_floor())
