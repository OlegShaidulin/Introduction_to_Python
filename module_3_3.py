def print_params(a = 1, b = 'string', c = True):
    print(a,b,c)
print_params()
print_params(1, False)
#print_params(1,2,3,4) ##TypeError: print_params() takes from 0 to 3 positional arguments but 4 were given

print_params(b=25)
print_params(c =[1,2,3])

value_list = [1,'string',True]
value_dict = {'a':1,'b':'string','c':True}
print_params(*value_list)
print_params(**value_dict)

value_list_2 = [2, 'str']
print_params(*value_list_2, False)