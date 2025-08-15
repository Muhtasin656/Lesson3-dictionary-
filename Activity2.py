dict_test={"value1":1,"value2":2,"value3":1,"value4":2,"value5":1}
print(dict_test)
k=1
result=0
for key in dict_test:
    if dict_test[key]==k:
        result=result+1
print(f"The frequency of {k} is {result}")