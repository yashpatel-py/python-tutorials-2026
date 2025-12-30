# print("Hello\nWorld")

# ========== Most Common Escape Sequences
# 1) New line \n
# print("Line1\nLine2\nLine3")

# 2) Tab \t
# print("Name\tAge\tCity")
# print("Yash\t25\tChicago")

# 3) Backslash \\
# # Wrong
# print("C:\new\test")

# # Right
# print("C:\\new\\test")

# # Best
# print(r"C:\new\test")


# 4) Quotes inside strings
# print("He said \"Hello\" to me.")
# print('It\'s a geat day!')

# 5) Carriage return \r
# print("Loading...\rDone!")

# 6) Backspace \b
# print("ABC\bD")

# 7) Form feed \f and vertical tab \v (rare)
# print("Hello\fWorld")
# print("Hello\vWorld")

# ========== The Invisible Bug
# path = r"C:\new\test" + "\\"
# print(path)

# import re
# pattern = r"\d+"
# print(pattern)

# ========== Raw Strings

# ========== Unicode Escape Sequences
# \u (4 hex digits)
# print("\u2764")

# \U (8 hex digits)
# print("\U0001F600")

# \N{...} (Unicode name)
# print("\N{ROCKET}")

# ========== Real-World Examples
# Multi-line message
# message = "Hi Yash,\nYour order has shipped!\nThanks,\nCodemiax"
# print(message)

# Table-like formatting
print("Name\tAge\tCity")
print("Yash\t25\tChicago")

# windows path
path1 = "C:\\Users\\Yash\\Documents\\file.txt"
path2 = r"C:\Users\Yash\Documents\file.txt"
print(path1)
print(path2)