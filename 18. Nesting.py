list = ["a", 1, [315, "fda"]]
print(list)

for i in list:
    print(i)

varlist = [i for i in list]
print(varlist)

dict = [{
    "Key1" : 1,
    "Key2" : {"Inner1" : 3, "Inner2" : 8,}
},
{   
    "Another" : "asdf",
    "Another2" : "qewr",
    }]
print(dict)