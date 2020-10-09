from TwoSums import twosums

length = int(input("Enter the length of the array : "))
nums = list()
for i in range(length):
    temp = int(input("Enter the number: "))
    nums.append(temp)

target = int(input("Enter the target : "))

solution = twosums(nums,target)
print("Output: ", solution)

