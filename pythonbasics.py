
# This is a formating trial
print("I love css2021.(upper)".upper()) # upper case, whole sentence
print("I love css2021.(rjust 20)".rjust(20)) # 
print("i love css2021.(capitalize)".capitalize()) # sentence case, capitalises first letter

# Concantenation (Addition)
print('I like' + str (' cs_class_codes ') + ('a lot!')) # addition
print(f'{print}(print function)')# print a function
print(f'{type(229)}(print type)')# returning a datatype

# Lists
list_1 = ['one,' 'two,' 'three']  # creating a list

list_1.append ('four')  # adding at the end

list_1.insert (0,'zero') # adding at the beginning

list_2 = [ 1, 2, 3]# creating a second list

list_1.extend (list_2) # adding two lists

print(list_1)

# Dictionary
siblings = {'Chelsea Esther,' 'Maureen Liberty,' 'Henry Duncun,' 'Jonathan McDonald'}

print(siblings)


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


