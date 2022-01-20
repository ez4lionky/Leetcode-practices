def findMedianSortedArrays(nums1: [int], nums2: [int]) -> float:
    l1, l2 = len(nums1), len(nums2)
    length = l1 + l2
    quotient = length // 2
    remainder = length % 2
    if l1 == 0:
        if remainder == 0:
            return (nums2[quotient - 1] + nums2[quotient]) / 2
        else:
            return nums2[quotient]
    elif l2 == 0:
        if remainder == 0:
            return (nums1[quotient - 1] + nums1[quotient]) / 2
        else:
            return nums1[quotient]

    nums = []
    idx1, idx2 = 0, 0
    for i in range(length):
        if idx1 == len(nums1) or idx2 == len(nums2):
            break
        else:
            if nums1[idx1] < nums2[idx2]:
                pre, cur = nums1[idx1], nums2[idx2]
                idx1 += 1
            else:
                pre, cur = nums2[idx2], nums1[idx1]
                idx2 += 1
            nums.append(pre)
    if idx1 == len(nums1):
        for i in range(idx2, l2):
            nums.append(nums2[i])
    else:
        for i in range(idx1, l1):
            nums.append(nums1[i])

    print(nums)
    if remainder == 1:
        return nums[quotient]
    else:
        return (nums[quotient - 1] + nums[quotient]) / 2


nums1 = [1, 2]
nums2 = [3, 4, 5, 6, 7, 8]
# nums1 = [2]
# nums2 = [1, 3, 4]
print(findMedianSortedArrays(nums1, nums2))
