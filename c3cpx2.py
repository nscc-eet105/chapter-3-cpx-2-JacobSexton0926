from adafruit_circuitplayground import cp
import time
while True:
    black = (0, 0, 0)
    for i in range(10):
        cp.pixels[i] = (100, 0, 0)
        time.sleep(.1)
        cp.pixels[i] = black
        time.sleep(.1)

    for i in range(9, 0,-1):
        cp.pixels[i] = (0, 0, 100)
        time.sleep(.1)
        cp.pixels[i] = black
        time.sleep(.1)
        # Write your code here :-)
