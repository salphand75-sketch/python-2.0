math = {"David","Rebbeca","Sam","Emily","John"}
english = {"Emily","Tomas","Lucas","Janice","Sam"}
science = {"Daniel","Steve","Rebbeca","Janice","Emily"}
print(math.intersection(english))
print(science.difference(english))
print(math.union(english).union(science))
print(math.intersection(english).intersection(science))
print(english.difference(math))
print(science.union(english).difference(math))
print(math.symmetric_difference(english))