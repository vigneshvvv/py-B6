def reverseList(sample):

    leftPointer = 0
    rightPointer = len(sample)-1

    while(leftPointer < rightPointer):
        temp = sample[leftPointer]
        sample[leftPointer] = sample[rightPointer]
        sample[rightPointer] = temp
        leftPointer += 1
        rightPointer -= 1

    print(sample)


nums = [10,20,30,40,50]
reverseList(nums)
