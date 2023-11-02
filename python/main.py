from datetime import datetime
import time


def my_function():
    while True:
        print("Hello World!\t" , datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
        time.sleep(1)

if __name__ == "__main__":
    my_function()