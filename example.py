import pytest


temperature = 10

def print_temperature():
  print(temperature)
def add(a, b):
    return a + b


def test_add():
    assert add(0.1, 0.2) == 0.3
