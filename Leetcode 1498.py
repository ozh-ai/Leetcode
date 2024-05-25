def numSubSeq(nums,target):
    for i in range(1,len(nums)): #sort array via insertion sort
        temp = nums[i]
        j = i-1
        while temp<nums[j] and j>=0:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = temp

    seq = 0
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i] + nums[j] <= target:
                seq += 1
                if j > i:
                    seq = seq + 2**(j-i-1) - 1
    return seq
                
print(numSubSeq([0,0,1,1,2,2,3,3,4,5,6,7,8,9,10,14],18))


