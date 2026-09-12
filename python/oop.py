# class std:
#     sub="python"
#     college="ABC"
#     year="3rd"
# std1=std()
# std2=std()
# print(std1.sub,std1.college)

'''constractor'''
# class student:
#     def __init__(self,name,cgpa): 
#         self.name=name
#         self.cgpa=cgpa
    
#     def getcgpa(self):
#         return self.cgpa

# stud1=student("himasnhu",9)
# stud2=student("ram",9.2)
# stud3=student("roshani",8.7)

# print(f"{stud1.name} has cgpa = {stud1.getcgpa()}")
# print(stud2.getcgpa())
# print(stud3.cgpa)


'''class/attributes'''
# class Student:
#     coll_name="abc"
#     pi=3.1
#     def __init__(self,name, sec):
#         self.name=name
#         self.sec=sec
#         self.pi=3.14
# s1=Student("ram",3)        
# print(s1.name)
# print(Student.coll_name)
# print(s1.pi)
# print(Student.pi)
        
        
'''instance method (self parameter ,access instace value as well as class ), 
   class method(parameter cls,access class attribute,use @classmethod to make instance),
   static method (no parameter,use for logic,@staticmetod )'''
# class Student:
#     coll_name="abc"
    
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#     @classmethod
#     def get_coll_name(cls):
#         print("college name in abc")
        
#     def get_info(self): #instance method
#         print(f"{self.name} is study in {Student.coll_name} at age of {self.age}")
        
        
#     @staticmethod
#     def add_age(age,extra_age):
#         final_age= age + extra_age
#         print(final_age)
    
# s1=Student("ram",19)

# print(s1.name)
# s1.get_coll_name()
# Student.get_coll_name()
# s1.add_age(19,5)



'''Design & create an online store for Products (name, price).
Track total products being created.
Create a static method to calculate discount on each product based on a % parameter.'''
# class store:
#     count=0
    
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#         store.count+=1
#     def get_info():
#         print(f"the price of {p1.name} is {p1.price}")
        
#     @classmethod
#     def get_count(cls):
#         print(f"total noumber of product is {cls.count}")
        
#     @staticmethod
#     def disc_price(price,disc):
#         final_price=price-(price*disc/100)
#         return final_price
        
    
# p1=store("book",50)
# p2=store("pen",10)
# p3=store("file",50)

# p1.get_count()
# print(store.disc_price(p2.price,10))


'''encapsulation'''
# class bank:
#     def __init__(self,name,income):
#         self.name=name
#         self._income=income

#     def get_balance(self):
#         return self._income

# A1=bank("ram",100000)

# print(f"name is : {A1.name} and salary is : {A1.get_balance()}")


'''inheritance'''
'''single level inheritance'''
# class employee:
#     start_time="9AM"
#     end_time="4PM"

# class teacher(employee):    
#     def __init__(self,name):
#         self.name=name
        
# class hod(employee):
#     modify_end_time="6PM"

# T1=teacher("atul")
# print(f"{T1.name} + {T1.start_time} + {T1.end_time}")
# print(f"{T1.name} + {T1.start_time} + {hod.modify_end_time}")


'''multi level inheritance'''
# class Employee:
#     start_time="10am"
#     end_time="6pm"

# class AdminStaff(Employee):
#     def __init__(self, role):
#         self.role=role

# class Accountant(AdminStaff):
#     def __init__(self,salary,role):
#         super().__init__(role)
#         self.salary=salary

# acc1 = Accountant(25_000,"CA")

# print(acc1.role, acc1.salary,acc1.start_time,acc1.end_time)


'''multiple inhetitance'''
# class Teacher:
#     def __init__(self, salary):
#         self.salary=salary
# class Student:
#     def __init__(self,gpa):
#         self.gpa=gpa
# class TA(Teacher,Student):
#     def __init__(self, salary,gpa,name):
#         super().__init__(salary)
#         Student.__init__(self,gpa)
#         self.name=name
# ta1 = TA(15_000, 9.3,"Shradha")

# print(ta1.name,ta1.gpa,ta1.salary)


'''Abstraction
Hiding internal details & showing only essential features'''
# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass
# class Lion(Animal):
#     def make_sound(self):
#         print("Roar!")
# class Cow(Animal):
#     def make_sound(self):
#         print("Moo!")
# lion=Lion()
# lion.make_sound()
# cow=Cow()
# cow.make_sound()



'''polymrophism (Different forms)'''
'''funcion overridding'''
# class Employee:
#     def get_designation(self):
#         print("designation=Employee")

# class Teacher(Employee):
#     def get_designation(self):
#         print("designation=Teacher")

# t1=Teacher()
# t1.get_designation()


'''duck typing (walking like duck , tacking like duck)'''
# class Teacher():
#     def get_designation(self) :
#         print ("designation=Teacher")
# class Accountant ():
#     def get_designation(self) :
#         print("designation=Accountant")
# t1 = Teacher()
# t1. get_designation()
# acc1 = Accountant()
# acc1. get_designation()
