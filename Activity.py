dict1={"ID1":{

"name":"Jackson","class":"5","subject":"PE"
},
"ID2":{

"name":"Harry","class":"1","subject":"PDH"
},
"ID3":{

"name":"Jackson","class":"5","subject":"PE"
},}
result={}
for key,value in dict1.items():
    if value not in result.values():
        result[key]=value
print(result)