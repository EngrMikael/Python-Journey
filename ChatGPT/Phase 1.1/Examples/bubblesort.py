list = [10, 9, 1, 3]
n = len(list)


#this loop goes through everything and doesn't use the swap of tuples 
'''
for i in range(n):
   for j in range(n):
       if(list[i] < list[j]):
           temp = list[i]
           list[i] = list[j]
           list[j] = temp
           print("pass ", i+1, list)

print(list)
'''


for i in range(n):
   for j in range(0, n -i -1):
       if(list[j] > list[j + 1]):
           list[j], list[j + 1] = list[j + 1], list[j]
           print("pass with tuple", i+1, list)

print(list)