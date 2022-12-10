# while True:
#     num1 = input('num1: ')
#     num2 = input('num2: ')
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         print(num1/num2)
#     except Exception as e:
#         print(e)
        
#     except ZeroDivisionError:
#         print('write a new number, cannot divide by zero!')
#     except ValueError:
#         print('enter only numbers!')
#     except:
#         print('error')
#         continue
#     else:
#         print('succes!')
#     finally:
#         print('End calculating')

tuple1 = (1,4,5,67,546,'sdfsdf',214144.534)
print(tuple1, type(tuple1))
# tuple1[3]=7
# print(tuple1)

str1 = 'some text here'
list1 = [1,5,75464,'fdssd',True]
tuple3 = tuple(list1)
tuple2 = tuple(str1)

print(tuple2)
print(tuple3)

print(sorted(tuple2))

def func1():
    a= 123
    b= 46
    c= a*b
    return a,b,c
x,y,z = func1()
print(func1(),type(func1()))

print(x,y,z)



