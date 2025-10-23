# so in python there is a function called sort, sorted, and reverse 
# but it is quite limited, i tried to sort a matrix list 
# like in a 2d array but it did not sort it fully
matrix_of_list = [
    [23, 22, 15],
    [12, 11, 18],
    [32, 9, 6]
]

sorted_matrix = sorted(matrix_of_list)
print(sorted_matrix)

# I later found out that it is limited and must use
# a more complex logic than a built in funcion

# The line `flat = sorted(sum(matrix_of_list, []))` is flattening the 2D matrix `matrix_of_list` into
# a 1D list, sorting that list, and storing the sorted result in the variable `flat`.
flat = sorted(sum(matrix_of_list, [])) 
# The line `sorted_matrix = [flat[i:i+3] for i in range(0, len(flat), 3)]` is creating a new 2D matrix
# from the sorted 1D list `flat`. Here's a breakdown of what it does:
sorted_matrix = [flat[i:i+3] for i in range(0, len(flat), 3)]
print(f"fully sorted list: {sorted_matrix}")
