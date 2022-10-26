# from exceptions import WrongNameError
#
# class Student:
#     def __init__(self,name):
#         self.__name = name
# 
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self,name):
#         if name.isalpha():
#             self.__name = name.title()
#         else:
#             raise WrongNameError(name)
#
#     @name.deleter
#     def name(self):
#         print('Нельзя удалять')
#
#
# s = Student('aman')
# print(s.name)
# s.name = 'ruslan'
# print(s.name)
# del s.name
# print(s.name)


# class Student:
#     def __init__(self,name):
#         self.__name = name
#
#
#     def get_name(self):
#         return self.__name
#
#     def set_name(self,name):
#         if name.isalpha():
#             self.__name = name.title()
#         else:
#             raise WrongNameError(name)
#
#     def del_name(self):
#         print('Нельзя удалять')

    #name = property(get_name,set_name,del_name)


# s = Student('aman')
# print(s.name)
# s.name = 'ruslan'
# print(s.name)
# del s.name
# print(s.name)

# s =  Student('Aman')
# print(s.get_name())
# s.set_name('ruslan1')
# print(s.get_name())


# class Student:
#     def __init__(self, name):
#         self.student_name = name
#
# s = Student('Alex123')
# print(s.student_name)