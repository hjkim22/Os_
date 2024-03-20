number = 99

b_num = bin(number)
print(b_num)

# o_num = oct(number)
o_num = oct(int(b_num[2:]))
print(o_num)

h_num = hex(number)
print(h_num)