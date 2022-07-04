def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [5,3,8,4,2,1]
bubble_sort(nums)
print(nums)


def selection_sort(nums):

    for i in range(5):
        minpose = i
        for j in range(i,6):
            if  nums[j] < nums[minpose]:
                minpos = j



        temp = nums[i]
        nums = nums[minpos]
        nums[minpose] = temp

        print(nums)

nums = [5,3,8,6,7,2]
selection_sort(nums)
print(nums)
