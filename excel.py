# # with open('B-small-practice.in') as f:
# #     content = f.readlines()
# f = open('B-small-practice.in', 'r')

# print(f.readline())
# print(f.readline())
# print(f.readline())
# print(f.readline())

# words = content.pop(0).split()
# charset, result = set(), set()
# [charset.add(x) for x in content.pop(0).split()]
# for word in words:
#     found = True
#     for char in word:
#         if not char in charset:
#             found = False
#             break
#     if found: result.add(word)
# print(result)
# f = open('example.csv','w')
# headers = ["X", "Y", "Sum", "Diff", "Mult", "Div"]
# f.write(",".join(headers))

# for x in range(10):
#     for y in range(1, x):
#         f.write("%s,%s,%s,%s,%s,%s"%(x, y, x + y, x - y, x * y, x / y))
# f.close()
import csv
import json

with open('example.csv', 'w', newline = '') as csvfile:
    fieldnames = ['First name', 'Last name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    names = [['Ashu', 'trip'], ['abc', 'def'], ['dgh', 'dcd']]
    writer.writeheader()
    for name in names:
        row = json.loads('{"First name": "%s", "Last name": "%s"}'%(name[0], name[1]))
        writer.writerow(row)
# import csv

# with open('names.csv', 'w', newline = '') as csvfile:
#     fieldnames = ['first_name', 'last_name']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()
#     writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
#     writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
#     writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})