'''
# read the array input
nums = list(map(int, input().strip('[]').split(',')))

# read the target
target = int(input())

# loop through all pairs
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])
            break  # stop after finding one valid pair
'''


nums = list(map(int, input().strip('[]').split(',')))
print(nums)
target = int(input())
print(target)

for i in range(len(nums)):
    for j in range(i +1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])
        break
