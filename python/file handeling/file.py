''' read mode'''
# f=open("/Users/himanshusharma/Desktop/learning/AI:ML-AC/python/file handeling/sample.txt","r")

# data=f.read()
# print(data)
# f.close()


'''write mode'''
# f=open("/Users/himanshusharma/Desktop/learning/AI:ML-AC/python/file handeling/sample.txt","w")

# f.write("write operation performed")
# f.close()

'''append mode'''
# f=open("/Users/himanshusharma/Desktop/learning/AI:ML-AC/python/file handeling/sample.txt","a")

# f.write("\n append operation performed")
# f.close()


'''create new file'''
# f=open("/Users/himanshusharma/Desktop/learning/AI:ML-AC/python/file handeling/sample2.txt","x")

# f.write("write operation performed")
# f.close()

'''wth keyword (auto close file)'''
# with open("/Users/himanshusharma/Desktop/learning/AI:ML-AC/python/file handeling/sample.txt","r+") as f:

#     data=f.read()
# print(len(data))


'''delete file'''
import os

os.remove("/Users/himanshusharma/Desktop/learning/AI:ML-AC/python/file handeling/sample2.txt")
