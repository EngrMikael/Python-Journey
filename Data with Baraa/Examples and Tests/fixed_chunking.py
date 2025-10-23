flat = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_3 = [flat[i:i+3] for i in range(0, len(flat), 3)]
chunk_2 = [flat[i:i+2] for i in range(0, len(flat), 2)]
chunk_4 = [flat[i:i+4] for i in range(0, len(flat), 4)]
chunk_5 = [flat[i:i+5] for i in range(0, len(flat), 5)]
print("3:", chunk_3)
print("2:", chunk_2)
print("4:", chunk_4)
print("5:", chunk_5)
