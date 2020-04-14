import math
import os
import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greeting = "Hello, {}".format(who_to_greet)
    return greeting


# print(greet('World'))
# print(greet('Mohsin'))
r = requests.get("https://google.com")
print(r.status_code)
