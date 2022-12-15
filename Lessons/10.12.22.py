# while True:
#     num1 = input('num1: ')
#     num2 = input('num2: ')
#     try:
#         num1 = int(num1)
#         num2 = int(num2)
#         print(num1 / num2)
#     except Exception as e:
#         print(e)     
#     except ZeroDivisionError:
#         print('Cannot divide by zero! ')
#     except ValueError:
#         print('Enter only numbers!')    
#     except:
#         print('Error')
#         continue    
#     else:
#         print('Succes!')
#         break
#     finally:
#         print('End calculating')



tuple1 = (1,4,6,7,2,34,5,6,8,'sdf',1436.3568)

print(tuple1, type(tuple1))
# tuple1[3] = 7
print(tuple1)

str1 = 'Some text here'
list1 = [1,4,6,8,',adfg',235,True]
tuple2 = tuple(str1)
tuple3 = tuple(list1)
print(tuple2)
print(tuple3)

print(sorted(tuple2))


def func1():
    a = 10
    b = 15 
    c = a*b
    return a,b,c

x, y, z = func1()
print(func1(),type(func1()))

print(x,y,z)
