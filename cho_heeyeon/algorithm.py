nums = list(map(int, input("Input nums[] : ").split()))
target = int(input("Input target : "))

nums_copy = nums
answer = []

for i in range(0, len(nums)):
   if nums[i] < target :
       for j in range(i+1, len(nums)):
           sum = nums[i] + nums_copy[j]
           if sum == target:
               answer.append(i)
               answer.append(j)


print(answer)