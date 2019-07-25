# encoding=UTF-8

import sys
import time
f = None
try:
    f = open("poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 为了确保它能运行一段时间
        time.sleep(2)
except IOError:
    print("Could not find utils poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the utils.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the utils)")

with open("poem.txt") as f:
    for line in f:
        print(line, end='')