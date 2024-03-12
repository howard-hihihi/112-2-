print("-----------------------------------------------")
switch_dict = {"face": True, "five": False}
all_true = all(value for value in switch_dict.values())

if all_true:
    print("all true")
else:
    print("not all true")
print(switch_dict)

print("-----------------------------------------------")
switch_dict["face"] = True
switch_dict["five"] = True
all_true = all(value for value in switch_dict.values())
if all_true:
    print("all true")
else:
    print("not all true")
print(switch_dict)