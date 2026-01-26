# print(bin(13))

# print(int('1101', 2))

# print(0b1101)


# ------ AND (&)
# 0-1=0
# 1-0=0
# 0-0=0
# 1-1=1
# print(12&10)

# print(f"12 = {bin(12)}")
# print(f"10 = {bin(10)}")
# print(f"8 = {bin(8)}")


# -- Example (check number even or odd)
# num = 8

# if num & 1==1:
#     print(f"{num} is odd")
# else:
#     print(f"{num} is even")

# ----- OR (|)
# 0-0=0
# 0-1=1
# 1-0=1
# 1-1=1

# print(12|10)

# print(f"12 = {bin(12)}")
# print(f"10 = {bin(10)}")
# print(f"14 = {bin(14)}")

# ------ XOR (^)
# 0-0=0
# 0-1=1
# 1-0=1
# 1-1=0

# print(12^10)
# print(5^5)
# print(100^100)

## --- ecample, swap variable withougt creating variable
# a = 5
# b = 10

# print(f"Before: a={a}, b={b}")

# a = a ^ b
# b = a ^ b
# a = a^b

# print(f"After: a={a}, b={b}")

# NOT (~)

# print(~0)
# print(~1)
# print(~2)
# print(~5)
# print(~12)
# print(~10)
# print(~11)

# left shift (<<) (multiplication)
print(12<<4)

# Right shift (>>) (division)
print(24>>2)
print(12>>2)
print(20>>2)