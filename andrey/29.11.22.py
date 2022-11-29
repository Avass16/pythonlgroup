import random
# sum = 0
# for i in range (0,101):
#     sum += i
# print(sum)

# for i in range(1,498):
#     if i % 2 == 0:
#         print(i)
        
# 3

# list = [1,2,5,12,14,48,256,17]
# for i in list:
#     print(i)
# else: list.append('List over')

# 4

# print(list)
# list2 = []
# while len(list2) !=4:
#     z = input('Vvedite imya: ')
#     list2.append(z)
# print(list2)
    
# 5

# for int1 in range(0,6):
#     result = (int1*117 + 87)//13 * (21**int1)
#     print(result)

random_int = random.randint(1,100)
print(random_int)

z = 10
while z !=0:
    i = int(input('Угадай число: '))
    if i == random_int:
        print('Ты выйграл!')
        break
    elif i < random_int:
        print('Число меньше загадоного!')
    elif i>random_int:
        print('Число больше загадоного!')
    else:
        print('Вы ввели непонятные символы')
        continue
    print('Оставшиеся попытки:' + str(z-1))
    z -=1





