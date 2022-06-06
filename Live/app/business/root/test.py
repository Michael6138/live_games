
result = filter(lambda x: type(x) == int or x.isdigit() , [1, '122', 2])
print(list(result))