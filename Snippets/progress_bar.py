import sys
import time

for i in range(0,101):
    time.sleep(0.1)
    sys.stdout.write("{} [{}{}]\r".format(i, '#'*i, "."*(100-i)))
    sys.stdout.flush()
sys.stdout.write("\n")
