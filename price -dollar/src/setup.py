from get_info import Get_info
import os
import time

class Setup:
    def __init__(self, minute, iter):
        self.model = Get_info()
        self.minute  = minute
        self.iter = iter 
        self._start()
        os.system("clear")
        self._show_detail()
    

    def _start(self):
        for _ in range(0, self.iter):
            self.model.get_price()
            time.sleep(self.minute * 60)
    

    def _show_detail(self):
        print("csv saved in you device ✓ by name  <<price.csv>>")
        print("please follow me on : ")
        print("-------> instagram : parvvaresh")
        print("-------> twitter : parvvaresh")
        print("-------> linkedin : parvvaresh")
        print("\n", "\n", " **women**  **life**  **freedom** ")

