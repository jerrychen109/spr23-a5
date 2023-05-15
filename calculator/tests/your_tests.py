#!/usr/bin/env python3
from calculator_adapter import run


### ADD AT LEAST TWO TESTS HERE!
assert run("3 / 2").output == "1"
assert run("5 - 10").output == "-5"

###

print("All tests passed!")
