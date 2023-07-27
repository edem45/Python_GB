input_string = input("Введите строку").split()
dict_string = {}
out_string = ""
for el in input_string:
    if el not in dict_string:
        #print(el)
        out_string += f"{el} "
    else:
        #print(el, dict_string[el])
        out_string += f"{el}_{dict_string[el]} "
    dict_string[el] = dict_string.get(el, 0) + 1

print(out_string)