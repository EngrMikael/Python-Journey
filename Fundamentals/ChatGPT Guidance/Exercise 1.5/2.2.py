# creating a script with the concept of mutable and immutable in a pythonic way by appending values into a nested list using a function

# first we imported copy as always.

# we defined a funtion mutate that has a parameter named data

# inside the function we have data[0] which point into the index 0 and we append X while we also have a data[1] it points into index 1 and it changes the values into ['Y', 'Z']. and it returns data

# now we have our original nested list that has 2 index [0, 1]

# then for shallow it copies the inner list of original.
# then deep deepcopies the original
# and in result it takes the data returned from the function mutate

# now to understand the process and we can assign the values for each list:
# okay so since shallow only coppies the inner list we have now its value as 

# original = [[1, 2, 'X'], ['Y', 'Z']] it replaced the value of index 1 (the answer here is incorrect, the correct answer should be [[1, 2, 'X'], [3, 4]])
# shallow = [[1, 2, 'X'], ['Y', 'Z']]
# deep = [[1, 2], [3, 4]]
# result: [[1, 2, 'X'], ['Y', 'Z']]
# the comments above is my breakdown to this code below, and this is from ChatGPT but i tried to replicate and write the script based on this breakdown

import copy

def mutate(data):
    data[0].append(['X'])
    data[1] = ['Y', 'Z']
    return data

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
result = mutate(shallow)

print("original:", original)
print("shallow:", shallow)
print("deep:", deep)
print("result:", result)