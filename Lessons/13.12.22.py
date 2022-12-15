set1 = {1,2,3,4,5,5,4,3,2,1}

print(set1, type(set1))

set2 = set()

print(type(set2))


list1 = [1,2,3,4,5,6,'asdf',1312,1,2,3,4,67,0]
set3 = set(list1)

print(set3)

str1 = 'some text here'

set4 = set(str1)

print(set4)

set4.add(12)

print(set4)


set4.discard(' ')
print(set4)

set4.clear()
print(set4)

set5 = {1,2,3,4,5,6,7,8,9,10}

set6 = {5,6,7,8,9,10,11,12,13,14,15}

# set_union = set5.union(set6)
set_union = set5|set6

print(set_union)

# set_inter = set5.intersection(set6)
set_inter = set5 & set6

print(set_inter)
