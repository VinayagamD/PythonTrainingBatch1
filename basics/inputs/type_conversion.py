"""
Type Conversion in python
"""
s = "0111"
t = "0o10"
v = "0XFE"
print(int(s, 2))
print(int(s, 4))
print(int(s, 16))
s = "12.0"
print(float(s))
s = '4'
print(ord(s))
print(hex(56))
print(oct(8))
print(complex(10, 5))
print(chr(76))
