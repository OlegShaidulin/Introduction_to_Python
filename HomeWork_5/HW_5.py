immutable = 1, 'A', "string", True, 1.2,
print(immutable)
#immutable[0] += 1 ##// TypeError: 'tuple' does not support item assigment
mutable_list = [1,2,3,4,5]
print(mutable_list)

for i in range(len(mutable_list)): #используя цикл все значения списка умнжу на 2
    mutable_list[i] *=2

print(mutable_list)
