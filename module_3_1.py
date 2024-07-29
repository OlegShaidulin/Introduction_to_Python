calls = 0 

def count_calls():
    global calls
    calls +=1
def string_info(txt):
    string_ = str(txt)
    info_about_string = (len(string_), string_.upper(), string_.lower())
    count_calls()
    return info_about_string
def is_contains(txt, list_to_search):
    string_ = str(txt).lower()
    list_to_search = list(list_to_search)
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string_:
            res = True
            break
        else:
            res = False
            continue
    count_calls()
    return res
    
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)