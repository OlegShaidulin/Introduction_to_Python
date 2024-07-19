first = int(input("first num: "))
second = int(input("second num: "))
third = int(input("third num: "))

if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)