# list=[]
# for i in range(6):
#     list.append(i*i)
    
# print(list)


# sq=[ i*i for i in range(6) if i%2 !=0]
# print(sq)


num=[-1,4,-5,3,6,-3,7]
num=[0 if val<0 else val for val in num] 
print(num)