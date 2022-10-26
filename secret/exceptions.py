




class WrongNameError(Exception):
    def __init__(self,name,message=None):
        self.message = f'в имени {name} содержится что то кроме  букв'
        self.name = name
        super().__init__(self.message)

    def __str__(self):
        return self.message

# name = input('name : ')
#
# if name.isalpha():
#     print(f'hi {name}')
# else:
#     raise WrongNameError(name)



# class Error(Exception):
#     pass
#
# class ValueTooSmall(Error):
#     pass
#
# class ValueTooLarge(Error):
#     pass
#
# def quess_salary(salary)
#
#
# #salary = int(input('salary : '))
#     if salary < 3000:
#         raise ValueTooSmall('Слишкрм маленбкая зп')
#     elif salary > 7000:
#         raise ValueTooLarge('Слишком высокая зп')
#     else:
#         print('Ok')



# class NegValError(Exception):
#     pass
#
# number = input('Введите число')
# if int(number) < 0:
#     raise NegValError('Введите положительное число')
# else:
#     print(f'загадонное число {number}')
#
# answer = 10 - int(number)
# print(answer)
#