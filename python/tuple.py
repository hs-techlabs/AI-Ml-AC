'''it is immutable, repeted value ()'''
num=(12,13,14,15,16,13,17,13)
print(num)
# print(type(num))
# print(len(num))
# print(num[2:4])

# sum=0
# for val in num:
#     sum+=val
# print(sum)

print(num.index(13))
print(num.count(13))