from inspect import isfunction,ismethod
import psutil

for x, y in psutil.__dict__.items():
    if isfunction(y) is True:
        print("Function name is %s" % x)
    elif ismethod(y) is True:
        print("Method name is %s" % x)
    elif ismethod(x) is True:
        print("Method name is %s" % x)


print(psutil.net_if_stats())