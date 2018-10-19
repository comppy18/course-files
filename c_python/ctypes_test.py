from ctypes import CDLL, c_double
hw_lib = CDLL('hw_ctypes.so')
hw_lib.hw3.restype = c_double
s = hw_lib.hw3(c_double(.1), c_double(.2))
print(s, type(s))
