# FIRST INSTALL SPEEDTEST CLIENT
pip install speedtest-cli
import speedtest
s = speedtest.Speedtest()

import inspect

for method in inspect.getmembers(s, predicate=inspect.ismethod):
    print(method)
print(' Download speed:', s.download())
print(' Upload speed:', s.upload())


