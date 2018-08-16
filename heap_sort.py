def build_heap(nums):
    for i in range(len(nums)):
        if i == 0:
            continue
        if nums[i] > nums[i // 2]:
            j = i
            while j != 0 and nums[j] > nums[j // 2]:
                tmp = nums[j]
                nums[j] = nums[j//2]
                nums[j//2] = tmp
                j //= 2

def heap_sort(nums):
    for j in range(len(nums)-1, -1, -1):
        tmp = nums[0]
        nums[0] = nums[j]
        nums[j] = tmp
        heap_down(nums, j)

def heap_down(nums, loc):
    i = 0
    while 1:
        left = i * 2
        right = left + 1
        if right < loc:
            j = left if nums[left] > nums[right] else right
            if nums[i] < nums[j]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i = j
            else:
                return
        elif left < loc:
            j = left
            if nums[i] < nums[j]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
                i = j
            else:
                return
        else:
            return

nums = [1, 4, 2, 5, 3]
build_heap(nums)
heap_sort(nums)
print(nums)
    
            