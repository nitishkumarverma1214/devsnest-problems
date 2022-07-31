num1 = [1,3,4,5,6,7]
num2 = [2,4,6,8,10,12]


len1 = len(num1)
len2 = len(num2)
nums = [0] *(len1 + len2)
ind =0
ind1 ,ind2 = 0,0
while(ind1< len1 and ind2 <len2):
    if num1[ind1] <= num2[ind2]:
        nums[ind] = num1[ind1]
        ind1 +=1
    else:
        nums[ind] = num2[ind2]
        ind2 +=1
    ind +=1
while(ind1 < len1):
    nums[ind] = num1[ind1]
    ind1 +=1
    ind +=1

while(ind2 < len2):
    nums[ind] = num2[ind2]
    ind2 +=1
    ind +=1

print(*nums)
n = len(nums)
median = nums[n//2] if n%2 !=0 else (nums[n//2 -1] + nums[n//2]) /2
print("median = %f"%median)