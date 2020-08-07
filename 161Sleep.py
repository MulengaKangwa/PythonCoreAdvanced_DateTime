from datetime import date
import time

ldates = []

d1=date(2015,1,19)
d2=date(2017,10,19)
d3=date(2016,12,19)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

time.sleep(2)

for d in ldates:
    print(d)