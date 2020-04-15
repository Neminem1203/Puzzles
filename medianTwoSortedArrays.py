# https://leetcode.com/problems/median-of-two-sorted-arrays/
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    listLen = (len(nums1)+len(nums2))
    p1 = 0
    p2 = 0
    i = 0
    even = listLen%2 == 0
    goal =  (listLen / 2)-1 if even else (listLen-1)/2
    while((p1 < len(nums1) and p2 < len(nums2)) and i < goal):
        if(nums1[p1] < nums2[p2]):
            p1 += 1
        else:
            p2 += 1
        i+= 1
    firstNum = 0
    if(p1 >= len(nums1)):
        firstNum = nums2[p2+(goal-i)]
        p2 += 1
    elif(p2 >= len(nums2)):
        firstNum = nums1[p1+(goal-i)]
        p1 += 1
    else:
        if(nums1[p1] < nums2[p2]):
            firstNum = nums1[p1]
            p1 += 1
        else:
            firstNum = nums2[p2]
            p2 += 1
    if not even:
        return firstNum
    else:
        if (p1 >= len(nums1)):
            return (firstNum + nums2[p2 + (goal - i)])/2
        elif (p2 >= len(nums2)):
            return (firstNum + nums1[p1 + (goal - i)])/2
        else:
            if (nums1[p1] < nums2[p2]):
                return (firstNum + nums1[p1])/2
            else:
                return (firstNum + nums2[p2])/2



print(findMedianSortedArrays([1,2,3,4], [3,4,5,6]))