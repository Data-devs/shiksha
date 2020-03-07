# s = {}
# a = ['a','b']
# b = [10,20]
# for i in range(2):
#     s[a[i]] = b[i]
#
#
# print(s.keys())

s = {}
a = ['amit kj','Bts love']
b = [10,20]
k= []
for i in range(2):
    s[a[i]] = b[i]


print(s.keys())

for i in s:
    j = i.replace(' ','_')

    k.append(j.lower())
print('k ')
print(k)

#

