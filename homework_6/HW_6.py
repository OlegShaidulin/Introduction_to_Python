#Работа со словарями:

my_dict = {"Den" : 2000, "Andrey": 1999}
print("Dict: ",my_dict)
print("Existing value: ",my_dict["Den"],"Not existing", my_dict.get("Alex"))
my_dict.update({"Sasha": 1999, 'Maks':1998})
print("Deleted value:",my_dict.pop("Andrey"))
print("Modified dict: ", my_dict)

#Работа с множествами:

my_set = {1 ,2 ,3, "4" , 1 ,2.3 ,4 , True}
print("Set: " , my_set)
my_set.update([5 , "6"])
my_set.discard(1)
print("Modified set: ", my_set)