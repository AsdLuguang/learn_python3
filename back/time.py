#!/usr/bin/python3

import time

currentTime = time.time();

totalSeconds = int(currentTime);
Second = totalSeconds % 60;

totalMinutes = totalSeconds // 60;
Minute = totalMinutes % 60;

totalHours = totalMinutes //60;
Hour = totalHours % 24;

print("%d:%d:%d" % (Hour, Minute, Second));

#print (currentTime);
