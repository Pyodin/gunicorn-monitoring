import requests
import random as rd
import time


if __name__ == "__main__":
    while True:
        random = rd.randint(0, 100)
        instance = 8000 + random % 3
        for i in range(random):
            r = requests.get(f"http://localhost:{instance}")
        time.sleep(1)
        
