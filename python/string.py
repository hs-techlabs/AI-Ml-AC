'''string is immutable'''

# word1="hello"
# word2="python"

'''length of word'''
# print(len(word1))

'''concetinate of words'''
# sentence=word1+" "+ word2
# print(sentence)

'''position index'''
# print(word1[3])

# for ch in word1:
#     print(ch)

'''slicing'''
# print(sentence[2:7])
# print(sentence[2:])
# print(sentence[-8:-3])

'''formating'''
a=5
b=7
# sum=a+b
'''normal formating'''
# print("sum of {} and {} is :{}".format(a,b,sum))  

'''index fromating'''
# print("sum of {1} and {0} is :{2}".format(a,b,sum))  

'''value formating'''
# print("sum of {a} and {b} is :{sum}".format(a=5,b=7,sum=a+b)) 

'''f-string'''
print(f"sum of {a} and {b} is {a + b}")