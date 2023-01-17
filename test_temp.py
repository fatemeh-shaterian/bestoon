import pytest

def f(a):
  a = a+1
  return a
def test_f():
  assert f(3) == 4
  
 
