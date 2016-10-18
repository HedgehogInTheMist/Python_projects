data = [5, 5, 5, 5, 5]
result = []
# for el in data:
#     if data.count(el) > 1:
#         result.append(el)
result = [el for el in data if data.count(el) > 1]
print(result)