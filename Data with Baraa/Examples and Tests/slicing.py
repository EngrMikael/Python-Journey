nums = [10, 20, 30, 40, 50, 60]

print(nums[0:3])
print(nums[-2:])
print(nums[1::2])
print(list(nums[i] for i in range(len(nums) -1, -1, -1)))


# exercise lvl 1.2 
# answer:
#  20, 30, 40, 50
# 10, 20, 30, 40
# 30, 40, 50, 60
# 40, 50
# 10, 30, 50
# 60, 40, 20
