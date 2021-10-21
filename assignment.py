#Assignment

# Mapping a dictionary
#siblings = (1: Name, 2: Age)

siblings1_keys = (1,2,3,4) 

siblings1_values = ('Name', 'Age', 'Sex', 'Family order')

siblings1 = dict(zip(siblings1_keys, siblings1_values))

print(siblings1)


#updating a dictionary
dict_1 = {'apples,' 'oranges,' 'pears,' 'berries'}

dict_2 = {'paw paws,' 'vanilla'}

dict_1.update(dict_2)
print(dict_1)


#iterating a dictionary
dict = {'Name': 'Aladina', 'age': 16, 'Home': 'Kamwokya'} 

for key in dict:

 print('key=',key)

print('value=',dict[key])


