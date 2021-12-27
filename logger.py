import time
from datetime import datetime

class Logger:
    def __init__(self):
        self.id =str(datetime.now()).split('.')[0].replace(' ','_').replace(':','-')
        self.path = f"./logs/{self.id}.log"
        f = open(self.path, "a")
        f.write(f"Init at {self.id}")
        f.close()

    def write_log(self):
        pass

