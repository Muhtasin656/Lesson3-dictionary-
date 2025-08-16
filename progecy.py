test_dict={"value1":34,"value2":34,"value3":45,"value4":87,"value5":74}
print(test_dict)
i=34
result=0
for key in test_dict:
    if test_dict[key]==i:
        result=result+1
print(f"The frequency of {i} is {result}")