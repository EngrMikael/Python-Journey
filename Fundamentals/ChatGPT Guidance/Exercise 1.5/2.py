# creating a script with the concept of mutable and immutable in a pythonic way by appending values into a nested list

#we imported the library copy into our script

# initiated x
# we used copy to y from x
# and deepcopy to z from x

# so we used a nested list not just a list therefore, we have 0 and 1 as our index.
# in index 0 of the x list we appended 99 so the value now of x is [[1, 2, 99] ,[3, 4]]

# then we also append [5, 6] this is where it gets unclear for me since i never encountered this problem or formula now, based on my understanding i formulated a hypothesis where in the value of x is not [[1, 2, 99], [3, 4], [5, 6]. now originally the only index we had for is is 0 and 1 but since we appended [5, 6] we created index 2

# now based on that explanation i can hypothetically give the output 

# x: [[1, 2, 99], [3, 4], [5, 6]]
# y: [[1, 2, 99], [3, 4], [5, 6]] # in this part i am quite unsure since we never really discussed copy only we skipped to deepcopy so this is my hypothetical answer
# z: [[1, 2], [3, 4]] # but here i am sure that this is the correct answer since it deepcopied the x first before appending anything to it
# the comments above is my breakdown to this code below, and this is from ChatGPT but i tried to replicate and write the script based on this breakdown
import copy

x = [[1, 2], [3, 4]]
y = copy.copy(x)
z = copy.deepcopy(x)

x[0].append(99)
x[1].append([5, 6])

print("x:", x)
print("y:", y)
print("z:", z)