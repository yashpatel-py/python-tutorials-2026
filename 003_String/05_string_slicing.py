# =============================== BASIC SLICING SYNTAX
# Syntax: String[start:end or stop]
# Start is Included
# end is not included

# word = "Python"
# print(word[0:2])

# String: P y t h o n
# Index:  0 1 2 3 4 5
#         [0:3] = "Pyt"
#          ^^^
#       (0, 1, 2)

# print(word[1:4])
# print(word[0:5])

# =============================== ADVANCED SLICING - LEAVING OUT PARAMETERS
# word = "Python"
# print(word[2:])
# print(word[:3])
# print(word[:])

# Example
# email = "john.doe@example.com"
# username = email[:email.find("@")]
# print(username)

# =============================== NEGATIVE SLICING - SLICING FROM THE END
# word = "Python"
# print(word[-3:])
# print(word[:-2])
# print(word[-5:-2])

# String: P y t h o n
# Index:  0 1 2 3 4 5
# Neg:   -6-5-4-3-2-1
#             [-3:] = "hon"
#              ^^^
#           (indices -3, -2, -1)

# =============================== STEP PARAMETER - SLICING WITH INTERVALS
# string[start:end:step]
word = "Python"
# print(word[::2])

# String: P y t h o n
# Index:  0 1 2 3 4 5
#         [::2] = "Pto"
#         ^   ^   ^
#      (every 2nd character)

# print(word[::1])
# print(word[::2])
# print(word[::3])
# print(word[1::2])

# print(word[::-1])
# print(word[5:0:-1])
# print(word[::-3])
# =============================== IMPORTANT CONCEPTS & EDGE CASES
word = "Python"
# CP - 1 - Slicing does not give error
# print(word[0:100]) 
# print(word[10:100])

# CP - 2 - String are Immutable
# word[0:2] = "Ja"
# print(word)

# word = "Ja"+word[2:]
# print(word)

# CP - 3 - Empty Slicing
print(word[3:3])
print(word[5:2])

# =============================== COMPLETE REFERENCE TABLE
# SYNTAX              EXAMPLE         RESULT          MEANING
# [start:end]         "Py"[0:2]       "Py"           From 0 to 2 (2 excluded)
# [start:]            "Py"[1:]        "y"            From 1 to end
# [:end]              "Py"[:1]        "P"            From start to 1
# [:]                 "Py"[:]         "Py"           Entire string
# [::step]            "Py"[::2]       "P"            Every 2nd character
# [::-1]              "Py"[::-1]      "yP"           Reversed
# [start:end:step]    "Py"[0:2:1]     "Py"           From 0 to 2, every 1
# [-n:]               "Py"[-1:]       "y"            Last n characters
# [:-n]               "Py"[:-1]       "P"            All except last n

# =============================== REAL-WORLD EXAMPLES
# Date processing
date = "2024-12-25"
year = date[0:4]
month = date[6:7]
day = date[9:10]

print(f"{day}/{month}/{year}")