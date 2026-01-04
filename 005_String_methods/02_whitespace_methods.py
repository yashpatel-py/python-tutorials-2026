# strip()
text = "     hello world.    "
print(text)
print(text.strip())

# lstrip()
print(text.lstrip())

# rstrip()
print(text.rstrip())

# TIP
text = "####Hello#########"
print(text.strip('#'))
print(text.lstrip('#'))
print(text.rstrip('#'))