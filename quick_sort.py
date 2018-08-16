def quick_sort(nums, left, right):
    if left == right or left + 1 == right:
        return
    i = partition(nums, left, right)
    quick_sort(nums, left, i)
    quick_sort(nums, i + 1, right)

def partition(nums, left, right):
    pivot = nums[left]
    i = left
    j = right-1
    while j > i:
        while i < j and nums[i] < pivot:
            i += 1
        while i < j and nums[j] > pivot:
            j -= 1
        if i != j:
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
    return i

nums = [1, 4, 2, 5, 3]
quick_sort(nums, 0, len(nums))
print(nums)