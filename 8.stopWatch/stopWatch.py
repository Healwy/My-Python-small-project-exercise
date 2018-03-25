#coding: utf-8

import time

print("Press Enter to begin ,Afterwards,Press Enter to click the stopWatch .")

input()
print("Start!")
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print("Lap #{}  :{} ({})".format(lapNum, lapTime, totalTime),end='')
        lapNum += 1
        lastTime = time.time()
except KeyboardInterrupt:
    print("Done")