x = int(input("км в первый день: "))
y = int(input("сколько хочется км в день: "))
i = 1
while x < y:
    x *= 1.1
    i += 1
print(i)